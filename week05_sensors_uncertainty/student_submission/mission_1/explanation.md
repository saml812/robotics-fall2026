# Mission 1

## bias

0.0029 

## bias_vs_variance

My prediction about what happens with a noisy sensor is correct. It should have a mean near 2.00 m, near-zero bias, and large variance. From the statstics, our mean = 2.0029 m, bias = 0.0029 m, variance = 0.0566 m², and median = 1.98 m. 
Bias and variance describe different failures because bias measures systematic displacement from the true value, while variance measures random scatter around the average. This sensor is unbiased but imprecise. A biased sensor would be consistently wrong but could still be precise; a noisy sensor can be correct on average but unreliable from reading to reading.

## dropouts

6

## mean

2.0029

## median

1.98 

## more_samples

More samples would not solve this sensor's main problem. It would reduce the standard error of the mean, making the average estimate more stable, but it would not reduce the sensor’s per-reading noise. The current standard deviation is about 0.238 m, with variance 0.0566 m², 6 dropouts, and 5 outliers. Even though bias is only 0.0029 m, the individual readings still scatter widely around 2.00 m. More samples would just add the same noisy distribution; they would not fix the main problem. 

## outliers

5

## prediction

I would predict that a biased sensor will have a sample mean shifted away from 2.00 meters and closer to the bias. The variance would remain small.
A noisy sensor will have a sample mean closer to 2.00 m because the random positive and negative errors will cancel each other out. Therefore, the bias is near zero, but there is large variance and a wide spread of readings. 
If the sensor is both biased and noisy, the mean will be shifted away from 2.00 m, and the spread will also be large. 
A biased sensor is inaccurate but can be precise, whereas a noisy sensor is imprecise but is unbiased.

## prediction_draft

I would predict that a biased sensor will have a sample mean shifted away from 2.00 meters and closer to the bias. The variance would remain small.
A noisy sensor will have a sample mean closer to 2.00 m because the random positive and negative errors will cancel each other out. Therefore, the bias is near zero, but there is large variance and a wide spread of readings. 
If the sensor is both biased and noisy, the mean will be shifted away from 2.00 m, and the spread will also be large. 
A biased sensor is inaccurate but can be precise, whereas a noisy sensor is imprecise but is unbiased.

## profile

noisy

## robot_consequence

One robot decision this could change is when to stop 2.00 m before an obstacle. Because the sensor is noisy, a single reading might be 1.80 m or 2.30 m even when the true distance is 2.00 m. If the robot trusts that reading, it might stop too late and cause a collision. It could also stop too early and block the road. For a person nearby, they could get injured in a collision or be confused by the erratic stopping.

## variance

0.0566 
