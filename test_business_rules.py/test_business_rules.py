from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


def test_calculate_license_cost():
    """Test the basic license cost calculation."""
    assert calculate_license_cost(40.00, 5) == 200.00


def test_calculate_license_cost_large_order():
    """Test license cost for a larger order."""
    assert calculate_license_cost(50.00, 100) == 5000.00


def test_no_discount_under_10_seats():
    """Test that orders under 10 seats receive no discount."""
    assert get_seat_discount(9) == 0.0


def test_discount_at_10_seats():
    """Test the discount at the 10-seat threshold."""
    assert get_seat_discount(10) == 0.07


def test_discount_at_49_seats():
    """Test the discount just below 50 seats."""
    assert get_seat_discount(49) == 0.07


def test_education_discount_at_50_seats():
    """Test the education discount at the 50-seat threshold."""
    assert get_seat_discount(50, True) == 0.16


def test_non_education_discount_at_50_seats():
    """Test the discount for non-education customers at 50 seats."""
    assert get_seat_discount(50, False) == 0.07


def test_license_total_with_onboarding_fee():
    """Test that the onboarding fee is added to a small order."""
    assert calculate_license_total(40.00, 5) == 260.00


def test_license_total_without_onboarding_fee():
    """Test a license total that does not require onboarding."""
    assert calculate_license_total(45.00, 60, False) == 2511.00


def test_license_total_education_discount():
    """Test the 16% education discount on a large order."""
    assert calculate_license_total(50.00, 150, True) == 6300.00


def test_onboarding_fee_at_400():
    """Test that a $400 license cost receives the onboarding fee."""
    assert calculate_license_total(100.00, 4) == 460.00


def test_no_onboarding_fee_above_400():
    """Test that costs above $400 do not receive an onboarding fee."""
    assert calculate_license_total(100.25, 4) == 401.00


def test_contract_review_at_5000():
    """Test that exactly $5000 does not require contract review."""
    assert needs_contract_review(5000.00) is False


def test_contract_review_above_5000():
    """Test that a total above $5000 requires contract review."""
    assert needs_contract_review(5000.01) is True


def test_trainer_at_25_seats():
    """Test that exactly 25 seats qualifies for a trainer."""
    assert gets_trainer(25, 750.00) is True


def test_no_trainer_below_threshold():
    """Test that 24 seats and a low total do not qualify for a trainer."""
    assert gets_trainer(24, 1339.20) is False


def test_trainer_above_3000():
    """Test trainer eligibility when the total exceeds $3000."""
    assert gets_trainer(9, 3600.00) is True


def test_trainer_at_3000():
    """Test that exactly $3000 does not qualify for a trainer."""
    assert gets_trainer(9, 3000.00) is False


def test_total_licensed():
    """Test the combined license total for multiple orders."""
    orders = [
        {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
        {
            "company": "Quarry School",
            "seat_price": 35.00,
            "seats": 12,
            "education": True,
        },
    ]

    assert round(total_licensed(orders), 2) == 710.60


def test_total_licensed_empty_orders():
    """Test that an empty orders list returns zero."""
    assert total_licensed([]) == 0.0


def test_largest_license():
    """Test that the largest license returns the correct company."""
    orders = [
        {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
        {
            "company": "Summit College",
            "seat_price": 50.00,
            "seats": 150,
            "education": True,
        },
    ]

    assert largest_license(orders) == "Summit College"


def test_format_license_line():
    result = format_license_line("Pine Books", 260.00, False, False)

    assert result == ("Pine Books: $260.00 | contract review: no | trainer: no")
