MIN_DISCOUNT_SEATS = 10
BULK_DISCOUNT_SEATS = 50
STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
ONBOARDING_THRESHOLD = 400
ONBOARDING_FEE = 60
CONTRACT_REVIEW_THRESHOLD = 5000
TRAINER_SEAT_THRESHOLD = 25
TRAINER_TOTAL_THRESHOLD = 3000
NO_DISCOUNT = 0.0
FULL_PRICE_RATE = 1.0


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Calculate the license cost before discounts."""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Return the discount rate based on seats and education status."""
    if seats < MIN_DISCOUNT_SEATS:
        return NO_DISCOUNT
    elif seats < BULK_DISCOUNT_SEATS:
        return STANDARD_DISCOUNT
    elif education:
        return EDUCATION_DISCOUNT
    else:
        return STANDARD_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Calculate the final license total including discounts and fees."""
    original_cost = calculate_license_cost(seat_price, seats)
    discount_rate = get_seat_discount(seats, education)
    discounted_cost = original_cost * (FULL_PRICE_RATE - discount_rate)
    if discounted_cost <= ONBOARDING_THRESHOLD:
        discounted_cost += ONBOARDING_FEE
    return discounted_cost


def needs_contract_review(total: float) -> bool:
    """Check whether the license total requires contract review."""
    return total > CONTRACT_REVIEW_THRESHOLD


def gets_trainer(seats: int, total: float) -> bool:
    """Check whether an order qualifies for a dedicated trainer."""
    return seats >= TRAINER_SEAT_THRESHOLD or total > TRAINER_TOTAL_THRESHOLD


def total_licensed(orders: list) -> float:
    """Calculate the combined license total for all orders."""
    total = NO_DISCOUNT
    for order in orders:
        total += calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
    return total


def largest_license(orders: list) -> str:
    """Return the company with the largest license total."""
    if not orders:
        return ""
    largest_company = ""
    largest_total = -FULL_PRICE_RATE
    for order in orders:
        current_total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        if current_total > largest_total:
            largest_total = current_total
            largest_company = order["company"]
    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """Format one customer's license report line."""
    review_text = "yes" if contract_review else "no"
    trainer_text = "yes" if trainer else "no"
    return f"{company}: ${total:.2f} | contract review: {review_text} | trainer: {trainer_text}"
