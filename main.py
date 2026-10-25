from business_rules import (
    calculate_license_total,
    format_license_line,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


def main():
    """Run the software license report."""
    orders = [
        {
            "company": "Pine Books",
            "seat_price": 40.00,
            "seats": 5,
            "education": False,
        },
        {
            "company": "Quarry School",
            "seat_price": 35.00,
            "seats": 12,
            "education": True,
        },
        {
            "company": "Redwood Cargo",
            "seat_price": 45.00,
            "seats": 60,
            "education": False,
        },
        {
            "company": "Summit College",
            "seat_price": 50.00,
            "seats": 150,
            "education": True,
        },
        {
            "company": "Tidal Health",
            "seat_price": 55.00,
            "seats": 100,
            "education": False,
        },
        {
            "company": "Upland Farms",
            "seat_price": 60.00,
            "seats": 24,
            "education": False,
        },
        {
            "company": "Vega Dental",
            "seat_price": 30.00,
            "seats": 25,
            "education": True,
        },
        {
            "company": "Willow Law",
            "seat_price": 400.00,
            "seats": 9,
            "education": False,
        },
    ]

    print("Cloudstep Software - Order Report")

    contract_reviews = 0
    trainers_assigned = 0
    for order in orders:
        total = calculate_license_total(
            order["seat_price"],
            order["seats"],
            order["education"],
        )
        contract_review = needs_contract_review(total)
        trainer = gets_trainer(order["seats"], total)
        report_line = format_license_line(
            order["company"],
            total,
            contract_review,
            trainer,
        )
        print(report_line)
        if contract_review:
            contract_reviews += 1
        if trainer:
            trainers_assigned += 1

    print(f"Orders: {len(orders)}")
    print(f"Total licensed: ${total_licensed(orders):.2f}")
    average_total = total_licensed(orders) / len(orders)
    print(f"Average license total: ${average_total:.2f}")
    print(f"Largest license total: {largest_license(orders)}")
    print(f"Contract reviews needed: {contract_reviews}")
    print(f"Trainers assigned: {trainers_assigned}")


if __name__ == "__main__":
    main()
