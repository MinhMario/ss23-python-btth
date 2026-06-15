from datetime import datetime


def evaluate_flex_time(book):
    if not book:
        print('Chưa có dữ liệu chấm công.')
        return

    print('\n--- ĐÁNH GIÁ VI PHẠM FLEX-TIME ---')

    LATEST_IN  = datetime.strptime('10:00', '%H:%M')
    WORK_HOURS = 9

    for r in book:
        nv_id    = r['id']
        time_in  = r['times'][0]
        time_out = r['times'][1]

        if time_out is None:
            print(f'{nv_id} - Chưa chấm công ra, bỏ qua đánh giá.')
            continue

        dt_in  = datetime.strptime(time_in,  '%H:%M')
        dt_out = datetime.strptime(time_out, '%H:%M')

        if dt_in > LATEST_IN:
            print(f'{nv_id} - Vi phạm: Đến muộn quá 90 phút.')
            continue

        worked_hours = (dt_out - dt_in).seconds / 3600
        if worked_hours < WORK_HOURS:
            print(f'{nv_id} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ.')
        else:
            print(f'{nv_id} - Hợp lệ: Hoàn thành ca làm việc.')