#!/usr/bin/env python
import decode_example

if __name__ == "__main__":
    # Sample data for our call:
    x, y = 6, 2.3

    encoded = 'DAAAAAAABgAKAAQABgAAAAwAAAAAAAYACAAEAAYAAAAEAAAABQAAAEwAAAA0AAAAJAAAABQAAAAEAAAA0P///4sCAAAAAHA93P///18AAAAAAJg96P///5kDAAAAAPg99P///3MCAAAAAPg9CAAMAAQACAAIAAAAUQIAAAAA+D0='

    decoded = decode_example.deserialize(encoded)

    print(f"INFERENCE DATA: {repr(encoded)}")
    print(f"DESERIALIZED: {repr(decoded)}")

    print('Finished')

