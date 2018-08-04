#!/usr/bin/env ruby

a=[1, 3, 2 , 2, 1]
b=[4, 2, 2 , 3, 3, 2 , 3 , 8]

def duplicates(a, b)
	result=[]
	counter={}

	for i in a 
		counter[i]=0
	end

	for j in b
		result << j unless counter[j].nil?
	end
	result
end

def intersection(a, b)
	result=[]
	counter={}

	for i in a 
		counter[i]=0 if counter[i].nil?
		counter[i]+=1
	end

	for j in b
		if not counter[j].nil? 
			result << j unless counter[j]<=0
			counter[j]-=1
		end
	end
	result
end

puts intersection(a,b).to_s