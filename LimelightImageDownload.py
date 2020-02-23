import urllib.request

lower_bound = int(input(print("Please enter the lower bound of the images")))
upper_bound = int(input(print("Please enter the upper bound of the images")))

for i in range(lower_bound, upper_bound):
    resource = urllib.request.urlopen("http://limelight-bottom:5801/snapshots/%s.jpg" % i)
    output = open("%s.jpg" % i, "wb")
    output.write(resource.read())
    output.close()