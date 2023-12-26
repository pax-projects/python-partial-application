import copy

def partial(func) -> callable:
	arguments: list[any] = []
	kwarguments : dict[any] = {}

	def wrapper(*args, **kwargs) -> str or any:
		if len(args) + len(kwargs) + len(arguments) + len(kwarguments) > func.__code__.co_argcount:
			raise TypeError(f"Too many arguments for {func.__name__}. The asked arguments are : {func.__code__.co_varnames}")
		#
		# Store arguments
		for arg in args: arguments.append(arg)
		for kwarg in kwargs: kwarguments[kwarg] = kwargs[kwarg] 

		# Verify arguments number compatibility
		if len(arguments) + len(kwarguments) == func.__code__.co_argcount:
			# Store temporary arguments to delete them after
			temp1 = copy.deepcopy(arguments)
			temp2 = copy.deepcopy(kwarguments)

			# Clear arguments stored
			arguments.clear()
			kwarguments.clear()

			# Call function
			return func(*temp1, **temp2)
		#
		return "Arguments function not completed..." # TO DO: Display remaining arguments
	#
	return wrapper
#
