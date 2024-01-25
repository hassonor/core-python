def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    one_step_before = 2
    two_steps_before = 1

    ways = 0

    for i in range(3, n + 1):
        ways = one_step_before + two_steps_before

        two_steps_before = one_step_before
        one_step_before = ways

    return ways


climb_stairs(3)
