# localtion.py
# A snippet to convert ref des/location from R1-3 -> R1,R2,R3 or R1-R3 -> R1,R2,R3
import re

def designator_split_dash(location_input):
    def split_text_and_number(s):
        temp = re.compile("([a-zA-Z]+)([0-9]+)")
        r = temp.match(s).groups()
        return r
        
    res = []
    if '-' in location_input:
        location_list = location_input.split('-')
        start_location = location_list[0]
        end_location = location_list[len(location_list)-1]
        
        # split text and number in a single location, this will be used to create the beginning of location range
        r = split_text_and_number(start_location)
        designator = r[0]
        start_range = int(r[1])
        
        # Because the end_range could be either x or Rx, an if-else block below will be used to check for x/Rx
        # x case
        if not end_location.startswith(designator):
            end_range = int(end_location)
        # Rx case
        else:
            r = split_text_and_number(end_location)
            end_range = int(r[1])
            
        for i in range(start_range, end_range+1):
            res.append(designator + str(i))
        return res

def designator_to_list(designators):
    res = []
    temp = designators.split(',')
    for i in range(len(temp)):
        if '-' in temp[i]:
            r = designator_split_dash(temp[i])
            res.extend(r)
        else:
            res.append(temp[i])
    return res
