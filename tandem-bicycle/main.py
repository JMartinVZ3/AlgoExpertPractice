redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1] 
fastest = True

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # The tandem speed
    speed = 0

    # We sort both of these lists to correctly pair the riders
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse = fastest)


    for i in range(len(redShirtSpeeds)):
        # The max function allows us to only sum the bigger number in these lists
        speed += max(blueShirtSpeeds[i], redShirtSpeeds[i])

    return speed


print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))