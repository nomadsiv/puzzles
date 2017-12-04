# coding=UTF-8
import sys


def sum_of_sequence(input_num_str):
    """
    Problem description at: http://adventofcode.com/2017/day/1

    >>> sum_of_sequence('34889')
    8
    >>> sum_of_sequence('348893')
    11
    >>> sum_of_sequence('3488933')
    14
    >>> sum_of_sequence('5255443714755555317777152441826784321918285999594221531636242944998363716119294845838579943562543247239969555791772392681567883449837982119239536325341263524415397123824358467891963762948723327774545715851542429832119179139914471523515332247317441719184556891362179267368325486642376685657759623876854958721636574219871249645773738597751429959437466876166273755524873351452951411628479352522367714269718514838933283861425982562854845471512652555633922878128558926123935941858532446378815929573452775348599693982834699757734714187831337546474515678577158721751921562145591166634279699299418269158557557996583881642468274618196335267342897498486869925262896125146867124596587989531495891646681528259624674792728146526849711139146268799436334618974547539561587581268886449291817335232859391493839167111246376493191985145848531829344198536568987996894226585837348372958959535969651573516542581144462536574953764413723147957237298324458181291167587791714172674717898567269547766636143732438694473231473258452166457194797819423528139157452148236943283374193561963393846385622218535952591588353565319432285579711881559343544515461962846879685879431767963975654347569385354482226341261768547328749947163864645168428953445396361398873536434931823635522467754782422557998262858297563862492652464526366171218276176258582444923497181776129436396397333976215976731542182878979389362297155819461685361676414725597335759976285597713332688275241271664658286868697167515329811831234324698345159949135474463624749624626518247831448143876183133814263977611564339865466321244399177464822649611969896344874381978986453566979762911155931362394192663943526834148596342268321563885255765614418141828934971927998994739769141789185165461976425151855846739959338649499379657223196885539386154935586794548365861759354865453211721551776997576289811595654171672259129335243531518228282393326395241242185795828261319215164262237957743232558971289145639852148197184265766291885259847236646615935963759631145338159257538114359781854685695429348428884248972177278361353814766653996675994784195827214295462389532422825696456457332417366426619555')
    1049

    :param num_str:
    :return:
    """
    relevant_nums = []
    prev_dig = input_num_str[len(input_num_str) - 1]
    for dig in input_num_str:
        # print "Previous digit: ", prev_dig, " Digit: ", dig
        if dig == prev_dig:
            relevant_nums.append(dig)
        prev_dig = dig

    # print "Digits matching previous in sequence: ", relevant_nums

    sum_relevant_digits = sum(int(digit) for digit in relevant_nums)
    return sum_relevant_digits


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    # input_arg = sys.argv[1]
    # print "Hello from the other side! You entered: ", input_arg
    # res = sum_of_sequence(input_arg)
    #
    # print "Sum of digits matching previous in sequence: ", res
    _test()