from os import path
import random
import uuid


def random_write(file_name):
    line_cnt = random.randint(1, 20)  # 修改多少行
    with open(file_name, "w+", encoding='utf-8') as f:
        lines = f.readlines(line_cnt)
        if len(lines) < line_cnt:
            content = [str(uuid.uuid1()) for i in range(0, line_cnt)]
            f.writelines('\n'.join(content))
        else:
            for i in range(0, line_cnt):
                lines[random.randint(1, line_cnt)] = str(uuid.uuid1())
            f.writelines(lines)


def main():
    file_types = ['.java', '.py', '.c']
    cur_path = path.dirname(path.abspath(__file__))
    write_file_cnt = random.randint(1, 10)

    for i in range(0, write_file_cnt):
        file_name = random.randint(0, 499)
        random_write("%s/src/%s%s" % (cur_path, file_name, random.choice(file_types)))


if __name__ == '__main__':
    main()
