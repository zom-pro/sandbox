#!/usr/bin/env bash
{
if [ ! $1 ]; then
    echo "Please provide path to your development virtual environment. Usage: ./build.sh path_to_venv"
    exit 0
fi
}

venv_path=$1
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
source $venv_path/bin/activate
pip --version
python setup.py sdist

# install from local library
pip install --upgrade $script_dir/dist/multiplier*.gz
python $script_dir/smoke_tests/smoke_test.py