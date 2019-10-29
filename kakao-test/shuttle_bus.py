"""4. Shuttle Bus in Python

카카오 신입 공채 코딩 테스트 문제
http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/

카카오에서는 무료 셔틀버스를 운행하기 때문에 판교역에서 편하게 사무실로 올 수 있다. 
카카오의 직원은 서로를 ‘크루’라고 부르는데, 아침마다 많은 크루들이 이 셔틀을 이용하여 출근한다.

이 문제에서는 편의를 위해 셔틀은 다음과 같은 규칙으로 운행한다고 가정하자.

셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 
예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
일찍 나와서 셔틀을 기다리는 것이 귀찮았던 콘은, 
일주일간의 집요한 관찰 끝에 어떤 크루가 몇 시에 셔틀 대기열에 도착하는지 알아냈다. 
콘이 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각을 구하여라.

단, 콘은 게으르기 때문에 같은 시각에 도착한 크루 중 대기열에서 제일 뒤에 선다. 
또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 
따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

[입력 형식]
셔틀 운행 횟수 n, 
셔틀 운행 간격 t, 
한 셔틀에 탈 수 있는 최대 크루 수 m, 
크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.

0 ＜ n ≦ 10
0 ＜ t ≦ 60
0 ＜ m ≦ 45

timetable은 최소 길이 1이고 최대 길이 2000인 배열로, 
하루 동안 크루가 대기열에 도착하는 시각이 HH:MM 형식으로 이루어져 있다.
크루의 도착 시각 HH:MM은 00:01에서 23:59 사이이다.


[출력 형식]
콘이 무사히 셔틀을 타고 사무실로 갈 수 있는 제일 늦은 도착 시각을 출력한다. 
도착 시각은 HH:MM 형식이며, 00:00에서 23:59 사이의 값이 될 수 있다.
"""


def time_to_board(n, t, m, table):
	"""Return latest time to board shuttle bus"""

	result = []

	# Time table for shuttle bus
	bus_table = []
	bus_hr = 9
	bus_min = 0
	for _ in range(n):
		if bus_min < 60:
			bus_table.append((bus_hr, bus_min))
		else:
			bus_hr += 1
			bus_min -= 60
			bus_table.append((bus_hr, bus_min))
		bus_min += t

	# Create list of valid crew in time order
	wait_list = [str_to_time(time) for time in table]
	for crew in wait_list:
		if crew > bus_table[-1]:
			wait_list.remove(crew)
	wait_list.sort()

	# After departure of each bus before last one, 
	# remove boarded crews from wait list
	if len(wait_list) > m:
		for bus in bus_table[:-1]:
			for i in range(m):
				if wait_list[i] <= bus:
					wait_list.remove(wait_list[i])
	
	# For the last bus
	if len(wait_list) < m : # Possible for no matter what
		result = [i for i in bus_table[-1]]
	else: # Need to arrive before the last crew
		last_crew = wait_list[:(m)][-1]
		if last_crew[-1] == 0:
			result.append(last_crew[0]-1)
			result.append(59)
		else:
			result.append(last_crew[0])
			result.append(last_crew[-1]-1)

	# convert result to string of time
	return time_to_str(result)


def str_to_time(str_time):
	"""Return tuple of two integers, (hr, min)"""

	crew_hr = int(str_time[:2])
	crew_min = int(str_time[-2:])

	return crew_hr, crew_min


def time_to_str(int_time):
	"""Return string result of given integer list of time"""

	if int_time[0] // 10 == 0:
		tt = '0'+ str(int_time[0])
	else:
		tt = str(int_time[0])
	if int_time[-1] // 10 ==0:
		mm = '0' + str(int_time[-1])
	else:
		mm = str(int_time[-1])

	return (tt + ':' + mm)


if __name__ == "__main__":
	input1 = [1, 1, 5, ['08:00', '08:01', "08:02", "08:03"], "09:00"]
	input2 = [2, 10, 2, ["09:10", "09:09", "08:00"], "09:09"]
	input3 = [2, 1, 2, ["09:00", "09:00", "09:00", "09:00"], "08:59"]
	input4 = [1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"], "00:00"]
	input5 = [1, 1, 1, ["23:59"], "09:00"]
	input6 = [
				10, 60, 45, 
				[
					"23:59","23:59", "23:59", "23:59", "23:59", "23:59",
					"23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
					"23:59", "23:59", "23:59", "23:59"
				],
				"18:00"
			]
	inputs = [input1, input2, input3, input4, input5, input6]
	
	# If the algorithm works for sample case, print True
	for item in inputs:
		n = item[0]
		t = item[1]
		m = item[2]
		table = item[3]
		result = item[4]

		print(time_to_board(n, t, m, table) == result)


