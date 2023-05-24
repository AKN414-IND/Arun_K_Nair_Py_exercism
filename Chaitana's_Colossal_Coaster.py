def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue
    else:
        raise ValueError("Invalid ticket_type. Must be 0 or 1.")

def find_my_friend(queue, friend_name):
    try:
        index = queue.index(friend_name)
        return index
    except ValueError:
        return -1

def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue

def remove_the_mean_person(queue, person_name):
    if person_name in queue:
        queue.remove(person_name)
    return queue

def how_many_namefellows(queue, person_name):
    count = queue.count(person_name)
    return count

def remove_the_last_person(queue):
    if len(queue) > 0:
        removed_person = queue.pop()
        return removed_person
    else:
        raise ValueError("Queue is empty.")

def sorted_names(queue):
    sorted_queue = sorted(queue)
    return sorted_queue
