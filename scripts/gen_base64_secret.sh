#!/bin/bash
string_value="$1"
output_name="$2"
usage="$0 <string_value> <output_file_name>"

function check_var(){
    if [[ -z "$1" ]]; then
        echo "error: $2 is missing"
        echo "$usage"
        exit 1
    fi
}

check_var "$string_value" "srting_value"
check_var "$output_name" "output_name"
echo -n $string_value | base64 > $output_name
