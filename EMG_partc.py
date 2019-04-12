from statistics import mean

partc_100_win = [21, 111]
partc_200_win = [16, 101]
partc_300_win = [19, 163]
partc_400_win = [13, 103]
partc_500_win = [6, 76]


def func(fName,arr):
    temp = open(fName, "r")
    fullArr = [i for i in temp.readlines()]
    temp.close()
    intergral = [float(i.split("\t")[2]) for i in fullArr if len(i) == 19]

    print(mean(intergral[arr[0]:arr[1]]))
    
func("partc_100.lvm", partc_100_win)
func("partc_200.lvm", partc_200_win)
func("partc_300.lvm", partc_300_win)
func("partc_400.lvm", partc_400_win)
func("partc_max.lvm", partc_500_win)