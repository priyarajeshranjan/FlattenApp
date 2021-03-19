def flatten_data(input):
    new_list = []
    for i in input:
        new_dict = {}
        for j in input[i]:
            new_dict[i+"_"+j]= input[i][j]
        if new_dict:
            new_list.append(new_dict)
    return new_list

