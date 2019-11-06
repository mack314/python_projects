def get_list_with_unique_items():
    tmp_list=[1,4,1,2,1,2,3,4,1,2,3,9,10,9,10]
    unique_list=list()

    while len(tmp_list)>1:
        list_of_index=list()
        first_item=tmp_list[0]
        print(first_item)
        for i in range(0,len(tmp_list)):
            if first_item == tmp_list[i]:
                list_of_index.append(i)
        unique_list.append(first_item)
        for i in range(0,len(list_of_index)):
            tmp_list.remove(first_item)
    unique_list.extend(tmp_list)   
    print(unique_list)



#Find all the unique elements of a list
def number_of_occurances():
    # Find the number of occurances of 1 in the list [1,2,1,2,1,2,3,4,1,2,3]
    tmp_list=[1,2,1,2,1,2,3,4,1,2,3]
    total_count_of_1=0
    for each_item in tmp_list:
        if each_item == 1:
            total_count_of_1=total_count_of_1+1
    print("total_count_of_1",total_count_of_1)

def print_memory_address_of_object(item):
    print("Memeory Address of ",item , "is :",id(item))

def main():
    test=2
    # print_memory_address_of_object(test)
    #number_of_occurances()
    get_list_with_unique_items()

main()