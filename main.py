from utils import get_data, get_filtered_data, get_sorted_data, get_formatted_data


def main():
    data = get_data('operations.json')
    data = get_filtered_data(data)
    data = get_sorted_data(data)
    for i in range(len(data)):
        data[i] = get_formatted_data(data[i])
        print(data[i])
        print()


if __name__ == '__main__':
    main()
