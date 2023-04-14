import random


def random_idx(list_length, sample_num):
    idx_list = [i for i in range(list_length)]
    sampled_idx = []
    while len(sampled_idx) < sample_num:
        idx = random.randint(0, len(idx_list) - 1)
        sampled_idx.append(idx_list[idx])
        del idx_list[idx]
    return sampled_idx


def random_list(input_list, sample_num):
    sampled_idx = random_idx(len(input_list), sample_num)
    sampled_list = []
    for idx in sampled_idx:
        sampled_list.append(input_list[idx])
    return sampled_list


def divide_train_val_txt(data_file, val_num, train_file, val_file):
    data_list = []
    with open(data_file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            line = line.rstrip()
            data_list.append(line)
    print(len(data_list))

    sampled_idx = random_idx(len(data_list), val_num)
    num_train = 0
    num_val = 0
    with open(train_file, 'w', encoding='utf-8') as ft:
        with open(val_file, 'w', encoding='utf-8') as fv:
            for idx in range(len(data_list)):
                if idx in sampled_idx:
                    fv.write(data_list[idx] + '\n')
                    num_val += 1
                else:
                    ft.write(data_list[idx] + '\n')
                    num_train += 1
    print(num_train, num_val)


if __name__ == '__main__':
    data_file = '/media/gaoxin/DATA/data/train_val/sly_dmyw/manifest.txt'
    train_file = '/media/gaoxin/DATA/data/train_val/sly_dmyw/train.txt'
    val_file = '/media/gaoxin/DATA/data/train_val/sly_dmyw/val.txt'
    divide_train_val_txt(data_file, 50, train_file, val_file)
