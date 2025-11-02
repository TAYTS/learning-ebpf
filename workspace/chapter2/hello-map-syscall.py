#!/usr/bin/python3
from bcc import BPF
from time import sleep
import sys

program = r"""
BPF_HASH(counter_table);

int hello(struct bpf_raw_tracepoint_args *ctx) {
   u64 opcode = ctx->args[1];
   u64 counter = 0;
   u64 *p;

   p = counter_table.lookup(&opcode);
   if (p != 0) {
      counter = *p;
   }
   counter++;
   counter_table.update(&opcode, &counter);
   return 0;
}
"""

b = BPF(text=program)

# Attach to a tracepoint that gets hit for all syscalls
b.attach_raw_tracepoint(tp="sys_enter", fn_name="hello")

try:
    while True:
        sleep(2)
        s = ""
        count = 0
        for k,v in b["counter_table"].items():
            s += f"OPCode {k.value}: {v.value}\t"
            count += 1
            if count % 4 == 0:
                s += "\n"
                count = 0
        print(s.strip())
        print("-----")
except KeyboardInterrupt:
    sys.exit(0)