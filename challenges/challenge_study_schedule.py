def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    counter = 0

    for item in permanence_period:
        if (
            None in item
            or isinstance(item[0], str)
            or isinstance(item[1], str)
        ):
            return None

        if item[0] <= target_time <= item[1]:
            counter += 1

    return counter
