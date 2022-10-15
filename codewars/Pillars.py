def pillars(num_pill, dist, width):
    x = num_pill * dist * 100 + num_pill * width - width * 2 - dist * 100
    return x if x > 0 else 0