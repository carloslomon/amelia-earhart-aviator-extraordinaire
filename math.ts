let variable = 0
let found = false

namespace Math {

    //% block="$input1 is between $input2 and $input3"
    export function ifNumberIsBetweenInputs (input1: number, input2: number, input3: number) {
        variable = 0
        for (let index = 0; index < input3 - input2; index++) {
            if (input1 == input2 + (input3 - (input2 + variable))) {
                found = true
            }
        variable += 1
        }
        return found;
    }

}