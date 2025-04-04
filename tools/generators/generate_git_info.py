################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
This script generates a C header containing git information.

This header then is used by the C firmware build to make the git version control
information available in the resulting binary.

To enable git version information in the build, you must:
- Have git installed and available - Either:
    - Have "git" in your PATH for the Makefile to call
    - Set the $GIT environment variable for the Makefile to use instead of "git"
- Have python 3 installed and available - either:
    - Have "python" in your PATH for the Makefile to call
    - Set the $PYTHON environment variable for the Makefile to use instead of "python"
- Pass ENABLE_GIT_VERSION_INFO=1 to make
"""
import argparse
from datetime import datetime
import sys

header_file_template = """
/*******************************************************************************
* Copyright © $CURRENT_YEAR Analog Devices Inc. All Rights Reserved.
* This software is proprietary to Analog Devices, Inc. and its licensors..
*******************************************************************************/
/*
 * This code was generated, do not edit this file manually!
 */

#ifndef GIT_INFO_H_
#define GIT_INFO_H_

#define GIT_HASH         $GIT_HASH
#define GIT_DIRTY_FLAG   $GIT_DIRTY_FLAG
#define GIT_VERSION_INFO ((GIT_HASH & 0x0FFFFFFF) | (GIT_DIRTY_FLAG << 28))

#endif /* GIT_INFO_H_ */
"""



def main():
    parser = argparse.ArgumentParser(
        description="Generate a header file with git hash and dirty flag defined")

    parser.add_argument("git_hash", type=lambda x: int(x, 16))
    parser.add_argument("git_dirty", type=int)
    parser.add_argument("--output", default="src/GitInfo.h")

    args = parser.parse_args()

    # Sanity check inputs
    if not (type(args.git_hash) == int and 0 <= args.git_hash <= 0x0FFF_FFFF):
        print("Error: Git hash is not a seven digit hex number")
        sys.exit(1)
    if not (type(args.git_dirty) == int and args.git_dirty in [0, 1]):
        print("Error: Git dirty flag is neither 0 nor 1")
        sys.exit(1)

    # Output generation
    output_text = header_file_template.lstrip()
    output_text = output_text.replace("$CURRENT_YEAR",   datetime.now().strftime("%Y"))
    output_text = output_text.replace("$GIT_HASH",       f"0x{args.git_hash:08X}")
    output_text = output_text.replace("$GIT_DIRTY_FLAG", f"{args.git_dirty}")

    # Check whether the generated result matches the existing result
    try:
        with open(args.output, "rt", encoding="utf-8") as f:
            if f.read() == output_text:
                print(f"Skipping generation of {args.output} file - no changes")
                sys.exit(0)
    except OSError:
        pass

    with open(args.output, "wt", encoding="utf-8") as f:
        print(f"Generating {args.output}")
        f.write(output_text)

if __name__ == "__main__":
    main()
