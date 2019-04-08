class MonteCarloSampler:
	def __init__(self):
		pass

	def err(self, x):
	    err_x = 0
	    for i in range(125):
	        err_x += ((-1.0)**i) * (x**((2.0*i)+1))/(math.factorial(i)*((2*i)+1))
	    err_x = (2.0/math.sqrt(math.pi))*err_x
	    return err_x

	#Approximation to Gaussian Distribution CDF
	def Phi(self,x):
	    return 0.5*(1.0+self.err(x/math.sqrt(2.0)))

	#Inverve of Exponential CDF with parameter lambda_0
	def inverse_exp(self,x,lambda_0):
	    return -1.0*math.log(1.0-x)/float(lambda_0)

	#Exponential density
	def expo(self,x,lambda_0):
	    return lambda_0*math.exp(-lambda_0*x)

	#Gaussian density
	def phi(self,x):
	    return math.exp((-(x**2.0))/2.0)/math.sqrt(2.0*math.pi)

	def truncated_gaussian_sampler(self,n,c):
		Phi_c = self.Phi(c)
		lambda_0 = (c + math.sqrt((c**2.0)+4.0))/2.0
		b = math.exp(((lambda_0**2.0) - (2.0*lambda_0*c))/2.0)/(math.sqrt(2.0*math.pi)*lambda_0*(1.0-Phi_c))
		const = ((1-Phi_c)*b)
		samples = []
		while len(samples)<n:
			x_inv = np.random.uniform()
			x = self.inverse_exp(x_inv, lambda_0)
			r = (self.phi(x+c)/(self.expo(x,lambda_0))*const)
			coin = np.random.uniform()
			if coin<r:
				samples.append(x+c)
		return np.array(samples)

