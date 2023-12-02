import matplotlib.pyplot as plt
import numpy as np

#In the order of T,K,J,H,D

task1Misclicks = np.array([0,0,0,0,0])
task1Times = np.array([24,13,10,8,10]) #in seconds
task1Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task2Misclicks = np.array([0,0,0,2,0])
task2Times = np.array([60,24,16,32,13])
task2Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task3Misclicks = np.array([2,0,0,0,0])
task3Times = np.array([20,15,9,17,8])
task3Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task4Misclicks = np.array([2,0,0,0,3])
task4Times = np.array([26,3,3,9,8])
task4Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task5Misclicks = np.array([0,0,0,0,0])
task5Times = np.array([6,4,2,5,13])
task5Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task6Misclicks = np.array([0,0,0,0,0])
task6Times = np.array([11,4,2,6,8])
task6Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task7Misclicks = np.array([0,0,0,0,0])
task7Times = np.array([5,3,2,4,7])
task7Success = np.array(["Yes","Yes","Yes","Yes","Yes"])

task8Misclicks = np.array([3,0,0,3,1])
task8Times = np.array([85,27,12,47,21])
task8Success = np.array(["Yes","Yes","Yes","Yes","Yes"])


task1TimeMean = np.mean(task1Times)
task1TimeSTD = np.std(task1Times)
print("Task 1 Average Time to Complete: ",task1TimeMean)
print("Task 1 STD of Time to Complete: ",task1TimeSTD)

task2TimeMean = np.mean(task2Times)
task2TimeSTD = np.std(task2Times)
print("Task 2 Average Time to Complete: ",task2TimeMean)
print("Task 2 STD of Time to Complete: ",task2TimeSTD)

task3TimeMean = np.mean(task3Times)
task3TimeSTD = np.std(task3Times)
print("Task 3 Average Time to Complete: ",task3TimeMean)
print("Task 3 STD of Time to Complete: ",task3TimeSTD)

task4TimeMean = np.mean(task4Times)
task4TimeSTD = np.std(task4Times)
print("Task 4 Average Time to Complete: ",task4TimeMean)
print("Task 4 STD of Time to Complete: ",task4TimeSTD)

task5TimeMean = np.mean(task5Times)
task5TimeSTD = np.std(task5Times)
print("Task 5 Average Time to Complete: ",task5TimeMean)
print("Task 5 STD of Time to Complete: ",task5TimeSTD)

task6TimeMean = np.mean(task6Times)
task6TimeSTD = np.std(task6Times)
print("Task 6 Average Time to Complete: ",task6TimeMean)
print("Task 6 STD of Time to Complete: ",task6TimeSTD)

task7TimeMean = np.mean(task7Times)
task7TimeSTD = np.std(task7Times)
print("Task 7 Average Time to Complete: ",task7TimeMean)
print("Task 7 STD of Time to Complete: ",task7TimeSTD)

task8TimeMean = np.mean(task8Times)
task8TimeSTD = np.std(task8Times)
print("Task 8 Average Time to Complete: ",task8TimeMean)
print("Task 8 STD of Time to Complete: ",task8TimeSTD)

timeData = [task1Times,task2Times,task3Times,task4Times,task5Times,task6Times,task7Times,task8Times]
fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)
bp = ax.boxplot(timeData, vert = 0,showmeans=True)

ax.set_title('Task Times')
ax.set_xlabel('Total Time to Complete Task in Seconds')
ax.set_ylabel('Task Number')

plt.show()

misclickData = [task1Misclicks,task2Misclicks,task3Misclicks,task4Misclicks,task5Misclicks,task6Misclicks,task7Misclicks,task8Misclicks]

misclickSums = []
for list in misclickData:
    sum = 0
    for num in list:
        sum += num
    misclickSums.append(sum)


misclickLabels = ["Task 1","Task 2","Task 3","Task 4","Task 5","Task 6","Task 7","Task 8"]

plt.bar(misclickLabels,misclickSums)

plt.title("Total Number of Misclicks per Task")
plt.ylabel("Number of Misclicks")

plt.show()
