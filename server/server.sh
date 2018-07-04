#!/bin/bash

./server_professor_exist_course.py &
./server_professor_exist_period.py &
./server_public_get_container.py &
./server_course.py &
./server_public_get_courses.py &
./server_public_user_detail.py &
./server_professor_filter_by_professor_courses.py &
./server_create_container.py &
./server_professor_create_course.py &
./server_create_user.py &
./server_professor_create_period.py &
./server_delete_period.py
./server_delete_period_course.py
./server_professor_get_image.py &
./server_periods_by_administrator.py &
./server_delete_period_courses.py &
./server_public_exists_container.py &



