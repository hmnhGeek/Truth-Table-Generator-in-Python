import os
os.system('color 8E')
class TruthTable(object):
    def __init__(self):
        pass
    def bool_in_list(self, l, index):
        val = l[index]
        if 0 in l:
            if val == 0:
                l.pop(index)
                l.insert(index, 1)         #As the value is 0, adding 1 to it won't affect the previous value.
            else:
                l.pop(index)
                l.insert(index, 0)
                self.bool_in_list(l, index -1)       #As the value is 1, adding 1 here makes it 0 and previous one is to be operated same as this last index.
            return l
        else:
            return

    def truth_table(self, num):
        var_List = []
        for i in range(num):
            val = raw_input('Enter '+ str(i+1) + ' variable: ')
            var_List.append(val)
        rule = raw_input('Enter expression: ')
        rule = 'F = '+rule
        SET = [0 for i in range(num)]
        print
        print 'Truth table of ' + rule
        print 
        for j in range(2**num):
            for elem in range(num):
                exec(var_List[elem]+'='+str(SET[elem]))
                
            exec rule
            if F == False:
                print SET, 0
            elif F == True:
                print SET, 1
            else:
                print SET, F
            SET = self.bool_in_list(SET, num - 1)
        print

    def possibles(self, num):
        print
        print "All combination of values"
        print
        SET = [0 for i in range(num)]
        for j in range(2**num):
            print SET
            SET = self.bool_in_list(SET, num - 1)
        print
tt = TruthTable()

def run():
    try:
        cmd = raw_input('> ')
        exec cmd in globals(), locals()
    except TypeError:
        print 'Error <Traceback report// function// parameters or number of parameters are worng/>'
    except AttributeError:
        print 'Error <Traceback report// Attribute// no such attribute present in the class/>'
    except NameError:
        print 'Error <Traceback report// Declaration// the parameter(s) to function or the command to prompt is not declared/>'
    except:
        print 'Error <Traceback report// unidentified// an error has been detected but it is unidentified/>'
    run()

run()
