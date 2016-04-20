class Scheduler:
	list_of_jobs = []
	list_of_results = {}
	start_time = None
	timeout = None
	def __init__(self, list_of_jobs, list_of_volunteers, timeout):
		self.list_of_jobs = list_of_jobs
		self.list_of_volunteers = list_of_volunteers
		self.timeout = timeout

	def assign(self):
		start_time = time.time()
		assigned_list = {}
		unassigned_list = []
		if self.list_of_jobs != []:
			marker = 0
			for job in self.list_of_jobs:
				if marker < len(self.list_of_volunteers):
					assigned_list[job] = self.list_of_volunteers[marker]
					self.list_of_jobs.remove(job)
					marker += 1
				else:
					break
		return assigned_list, self.list_of_jobs

	def check_status(self):
		if list_of_jobs != []:
			return False
		else:
			return True

	def poll_jobs():
		if (time.time() - start_time) >= timeout:
			if assigned_list != {}:
				for job in assigned_list:
					unassigned_list.append(job)
					del assigned_list[job]

	def add_to_completed(self, job, result):
		if job in assigned_list:
			list_of_results[job] = result
			del assigned_list[job]

	def get_results(self):
		return list_of_results