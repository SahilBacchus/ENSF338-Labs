##### 1. Mention at least two aspects that make interpolation search better than binary search [0.1 pts]
##### One aspect that makes interpolation search better than binary search is that interpolation search often makes fewer comparisons than binary search because the "midpoint" is set to where the item is likely to occur. Another aspect is that interpolation search has a lower average case time complexity compared to binary search when it comes to uniformly distributed data. Interpolation search's average case time complexity is O(loglogn) while binary search's average case time complexity is O(logn).

##### 2. Interpolation search assumes that data is uniformly distributed. What happens when this data follows a different distribution? Will the performance be affected? Why? [0.2 pts]

##### When the data is not uniformly disitributed, interpolation search's performance will be affected negatively. This is because the search might miss the target of where the item is likely to occur completely if the data is non-uniformly spaced. This results in the function having to retrace and recheck a lot of irrelevanet positions, which ultimately slows down the process. 

##### 3. If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected? [0.1 pts]

##### The position calculation part of the code would be affected. This is because it assumes a uniform distribution between high and low values and then attempts to compute the position where the specified value is likely to be found. So the position calculation code would need to be adjusted based on the specific characteristics of the new distribution if we want to modify it to follow a different distribution.

##### 4. When is linear search your only option for searching data as binary and interpolation search may fail? [0.2 pts]

##### Linear search is the only option for searching data when the data is unsorted as binary search requires sorted data and interpolation search relies on data having a predictable distribution. On the contrary, linear search works with both sorted and unsorted data as it iterates through and checks each element one by one.

##### 5. In which case will linear search outperform both binary and interpolation search, and why? [0.2 pts]

##### When the data set is really small, linear search can outperform both binary and interpolation search. This is because the overhead for setting up the conditions for calculating midpoints or where the target item is most likely to occur may hinder the search time for super small datasets. This is why linear search is more efficient as it has low overhead and is very simplistic.

##### 6. Is there a way to improve binary and interpolation search to solve this issue? [0.2 pts]

##### To improve binary search to solve this issue, presort the data prior to performing the binary search. This is especially good if you are planning to perform multiple binary searches with the data afterwards. Although there is overhead for presorting the data, it would be more efficient in the long run and will be more efficient than binary searching unsorted data.

##### To improve interpolation search to solve this issue, preprocess the data to transform the dataset to a better, more uniform distribution prior to performing interpolation search. This will allow the interpolation search to be way more efficient as it would barely function with unsorted data/skewed distributions.

##### Lastly, caching the presorted/preprocessed datasets/search results can improve performances for both searches if the datset is static or rarely changes. This will result in some of the overhead being bypassed.