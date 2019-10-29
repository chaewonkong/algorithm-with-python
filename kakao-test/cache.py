"""3. Cache in python

From 1st Kakao coding test

[Input]
Cache size and array of cities are given.
Cache size is integer between 0 and 30 (0<=cacheSize<=30).
Maximum number of cities in cities array is 100,000.
Each city in array cities are consist of english alphabet both upper/lowercase.
Maximum length of city name is 20.

[Output]
Return net processing time if cities are processed in order.

[Condition]
Use LRU(Least Recently Used) as cache change algorithm.
Processing time for 'cache hit' is 1.
Processing time for 'cache miss' is 5.
"""


def run_time(cache_size, cities):
	"""Return runtime for given cache_size and array"""

	cache = {}
	cache_order = []
	time = 0

	if cache_size == 0:
		return (len(cities) * 5)

	for city in cities:
		city = city.lower()
		if city in cache:
			cache[city] += 1
			time += 1
		else:
			if len(cache_order) < cache_size:
				cache_order.append(city)
				cache[city] = 1
				time += 5
			else:
				i = 0
				while i <= cache_size:
					if cache[cache_order[i]] == min(cache.values()):
						cache.pop(cache_order.pop(i))
						cache_order.append(city)
						cache[city] = 1
						time += 5
						break
					else:
						i += 1

	return time


if __name__ == "__main__":
	test_cache = [3, 3, 2, 5, 2, 0]
	test_cities = [
					['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju',
					'Pangyo', 'Seoul', 'NewYork', 'LA'],
					['Jeju', 'Pangyo', 'Seoul', 'Jeju',
					'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'],
					['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
					'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju',
					'NewYork', 'Rome'],
					['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA',
					'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju',
					'NewYork', 'Rome'],
					['Jeju', 'Pangyo', 'NewYork', 'newyork'],
					['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']	

	]
	answers = [50, 21, 60, 52, 16, 25]

	for i in range(len(test_cache)):
		test = run_time(test_cache[i], test_cities[i])
		answer = answers[i]
		print("TEST:", test, "Answer:", answer, "Valid:", test==answer)