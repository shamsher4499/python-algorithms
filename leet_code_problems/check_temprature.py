given_temp = [75, 76, 77, 72, 34, 89]

# output = [1,1,3,2,1,0]
# list_data = []
# count = 0
# for i,j in enumerate(given_temp):
#     if j < given_temp[i+1]:
#         list_data.append(1)
#     else:
#         count+=1
#         while j < given_temp[i+count]:
#             ...


def generate_output(temperatures):
    output = []
    count = 0

    for i in range(len(temperatures) - 1):
        if temperatures[i] > temperatures[i-1]:
            output.append(1)
            count = 0
        else:
            count += 1
            output.append(count)

    return output

temperature = [75, 76, 77, 72, 34, 89]
output = generate_output(temperature)
print(output)
