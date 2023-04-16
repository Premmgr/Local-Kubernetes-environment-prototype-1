#!/bin/bash
key_comment="$1"
passphrase="$2"
output_name="$3"
usage="$0 <key_comment> <Passphrase> <output_name>"

function check_var(){
    if [[ -z "$1" ]]; then
        echo "error: $2 is missing"
        echo "$usage"
        exit 1
    fi
}

function generate_ssh_key(){
    ssh-keygen -t rsa-sha2-512 -C "${comment}" -P "${passphrase}" -f "${output_name}" -q

}

check_var "$key_comment" "key_comment"
check_var "$passphrase" "passphrase"
check_var "$output_name" "output_name"
generate_ssh_key
