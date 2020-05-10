# tape variables
TS_MAX=1000

# the digital tape model
class DTape:
    def __init__(self,size,alphabet,noopidx=0):
        if size>TS_MAX:
            self.size=TS_MAX
        else:
            self.size=size
        if len(alphabet)==0:
            raise Exception('alphabet has zero symbols')
        self.alphabet=alphabet
        self.data=[self.alphabet[noopidx] for x in range(self.size)]


class DTapeMC:
    def __init__(self,dtape,cmdmap,noopsym):
        self.tape=dtape
        self.thead=0
        self.cmdmap=cmdmap
        self.noopsym=noopsym
        self.jmpctr=1
    
    def process_cell(self):
        if self.thead>=len(self.tape.data) or self.thead<0:
            print('[TAPEBOUND_EXCEEDED] machine head @[%d] is beyond tape'%self.thead)
            return
        datum=self.tape.data[self.thead]
        print('evaluating: %s'%datum)
        if datum==self.noopsym:
            print('noop')
        else:
            eval(cmdmap[datum])
        self.thead+=self.jmpctr


class DTapeComputer:
    def __init__(self,dtapemc,casetteimg):
        self.tapemc=dtapemc
