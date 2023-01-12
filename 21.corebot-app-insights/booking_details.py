# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.


class BookingDetails:
    def __init__(
        self,
        dst_city: str = None,
        or_city: str = None,
        budget: str = None,
        str_date: str = None,
        end_date: str = None,
    ):

        self.dst_city = dst_city
        self.or_city = or_city
        self.budget = budget
        self.str_date = str_date
        self.end_date = end_date
