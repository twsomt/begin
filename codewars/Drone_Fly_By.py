def fly_by(lamps, drone):
    return lamps.replace('x', 'o', len(drone))


print(fly_by('xxxxxxxxx', '==T'))