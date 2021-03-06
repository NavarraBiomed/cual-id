from difflib import get_close_matches


def parse_ids(input_file, col):
    return [e.strip().split('\t')[col] for e in input_file]


def fix_ids(correct_input, input_to_check, thresh=.5):
    corr_ids = parse_ids(correct_input, 0)
    broke_ids = parse_ids(input_to_check, 0)

    seen = set()
    for broke_id in broke_ids:
        fixed_id = get_close_matches(broke_id, corr_ids, 1, thresh)
        if not fixed_id:
            fixed_id = ''
        else:
            fixed_id = fixed_id[0]

        err_code = get_err_code(broke_id, fixed_id, seen)
        seen.add(fixed_id)
        yield broke_id, fixed_id, err_code


def format_output(output, show):
    show = list(show)
    for line in output:
        if any(i in list(line[2]) for i in show):
            yield '\t'.join(line)


def get_err_code(broke_id, fixed_id, seen):
    if fixed_id == '':
        err_code = 'N'
    elif broke_id == fixed_id:
        err_code = 'V'
    else:
        err_code = 'F'
    if fixed_id != '' and fixed_id in seen:
        err_code = 'D' + err_code
    return err_code
