import json

def json_file_filter_list(term, column, file) :
    
    with open(file) as json_file:
        data = json.load(json_file)
        result = []
        for product in data:
            if term.lower() in product[column].lower() :
                result.append(product)

        return result


if __name__ == '__main__' :
    #filter for brand A
    filtered_list = json_file_filter_list(term = 'A', column = 'brand', file='list.json')
    
    with open('filtered_list', 'w') as json_file:
        json.dump(filtered_list, json_file)

    print(filtered_list)
    
    