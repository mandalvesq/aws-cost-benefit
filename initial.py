def cost_benefit_input():
    with open("1.txt", 'r') as input1:
        listed = []
        for line in input1.readlines():
            if 'HVM' in (line):
                it = line.split(',')[0]
                vcpu = line.split(',')[1]
                with open("2.txt", 'r') as input2:
                    for line1 in input2.readlines():
                        if it in (line1):
                            mem = line1.split(',')[1]
                            cost = line1.split(',')[2]
                            # Formula #
                            mem = float(mem)
                            vcpu   = float(vcpu)
                            cost = float(cost)
                            cost_benefit = (((mem / 3.75) + vcpu)/cost)
                            cost_benefit = round(cost_benefit, 0)
                        
                            listed.append((it,cost_benefit))
        return listed

def cost_benefit_output(listed):
    listed = sorted(listed, reverse=False, key=lambda it: it[1])
    with open("output.txt", 'a') as output:
        for i in listed:
            i = i[0]
            output.write(i+'\n')
def main():
    listed = cost_benefit_input()
    cost_benefit_output(listed)
   
   
if __name__ == "__main__":
    main()
