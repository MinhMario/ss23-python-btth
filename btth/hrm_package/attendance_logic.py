def clock_in(book):
    nv_id = input('Nhập mã nhân viên: ').strip().upper()

    for r in book:
        if r['id'] == nv_id:
            print(f'Lỗi: Mã {nv_id} đã tồn tại trong hệ thống!')
            return

    name = input('Nhập tên nhân viên: ').strip()
    time_in = input('Nhập giờ vào (HH:MM): ').strip()

    book.append({
        'id': nv_id,
        'name': name,
        'times': (time_in, None)
    })
    print(f'Thành công: Đã ghi nhận {nv_id} chấm công vào lúc {time_in}!')


def clock_out(book):
    if not book:
        print('Chưa có dữ liệu chấm công.')
        return

    nv_id = input('Nhập mã nhân viên: ').strip().upper()

    for r in book:
        if r['id'] == nv_id:
            if r['times'][1] is not None:
                print(f'Lỗi: {nv_id} đã chấm công ra lúc {r["times"][1]}!')
                return
            time_out = input('Nhập giờ ra (HH:MM): ').strip()
            r['times'] = (r['times'][0], time_out)
            print(f'Thành công: Đã ghi nhận {nv_id} chấm công ra lúc {time_out}!')
            return

    print('Không tìm thấy nhân viên!')