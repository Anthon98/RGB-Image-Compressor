import string
import itertools
import logging


logging.basicConfig(level=logging.DEBUG)

values = []
uids = []

for digits in range(0, 5):
    # Should give a 17 million range out of RGB's possible 16,777,216 range.
    for uid in itertools.product(string.ascii_letters + string.digits + '-.', repeat=digits):
        uids.append(''.join(uid))

# This nested loop can probably be 'code golfed' with itertools as well.
idx = 0
for a in range(0, 255+1):
    for b in range(0, 255+1):
        for c in range(0, 255+1):
            # Making this into a dictionary or nesting these values will cause very slow code execution unfortunately.
            values.append((a, b, c, uids[idx]))
            idx += 1

fake_json_example = {
    'picture': {
        'pixels': [
            (0, 255, 255),
            (255, 255, 0),
            (126, 23, 50),
            (250, 3, 77),
        ]
    }
}

formatted = {}
for count, rgb in enumerate(fake_json_example['picture']['pixels']):
    for rgbg in values:
        # This statement could look nicer if performance could be faster (check pervious comment as to why).
        if rgb[0] == rgbg[0] and rgb[1] == rgbg[1] and rgb[2] == rgbg[2]:
            logging.info("Found match for %s, compressing it to: %s" % (rgb, rgbg[3]))
            fake_json_example['picture']['pixels'][count] = rgbg[3]
            break

logging.info("Complete compressed list: %s" % fake_json_example)

# So say we have a string with our compressed pixel data in Lua, mapped with our UID, we can find its RGB like so:
for compressedData in fake_json_example['picture']['pixels']:
    for rgb in values:
        if compressedData in rgb:
            logging.info("Decoded %s as : %s %s %s" % (compressedData, rgb[0], rgb[1], rgb[2]))
            break