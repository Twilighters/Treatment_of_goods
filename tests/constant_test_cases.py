# публичные тестовые случаи из текста условия задачи
PUBLIC_TEST_CASES = [
    {
        "test_input": {
            "id": 123,
            "name": "Телевизор",
            "package_params": {"width": 5, "height": 10},
            "location_and_quantity": [
                {"location": "Магазин на Ленина", "amount": 7},
                {"location": "Магазин в центре", "amount": 3},
            ],
        },
        "expected": None,
    },
    {
        "test_input": {
            "id": 123,
            "name": "Телевизор",
            "package_params": {"width": 55, "height": 100},
            "location_and_quantity": [
                {"location": "Магазин на Ленина", "amount": 777},
                {"location": "Магазин в центре", "amount": 3},
            ],
        },
        "expected": None,
    },
    {
        "test_input": {
            "id": 456,
            "name": "свитч",
            "package_params": {"width": 50, "height": 100},
            "location_and_quantity": [
                {"location": "Магазин на Ленина", "amount": 70},
                {"location": "Магазин в центре", "amount": 30},
            ],
        },
        "expected": None,
    },
    {
        "test_input": {
            "id": 456,
            "name": "свитч",
            "package_params": {"width": 50, "height": 100},
            "location_and_quantity": [
                {"location": "Магазин на Ленина", "amount": 70},
                {"location": "Магазин в центре", "amount": "30"},
            ],
        },
        "expected": None,
    },
    # {"test_input": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "expected": 0},
    # {"test_input": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "expected": 1},
]

# Здесь можно написать свои тестовые случаи
SECRET_TEST_CASES = []
