#
# Makefile
#
CC = gcc
#CFLAGS = -Wall -Wshadow -Wundef -Wmaybe-uninitialized
CFLAGS = -Wall -Wshadow -Wundef -fPIC
CFLAGS += -O3 -g3 -I./lib
CFLAGS += `pkg-config --cflags gtk+-3.0`
BIN = demo
VPATH =
LDFLAGS = `pkg-config --libs gtk+-3.0` -lpthread
LDFLAGS += -shared

LVGL_DIR = ${shell pwd}/lib
LVGL_DIR_NAME = lvgl

MAINSRC = main.c

#LIBRARIES
include ${shell pwd}/lib/lvgl/lvgl.mk

#DRIVERS
include ${shell pwd}/lib/lv_drivers/lv_drivers.mk

# include ./lv_examples/lv_examples.mk

OBJEXT ?= .o

AOBJS = $(ASRCS:.S=$(OBJEXT))
COBJS = $(CSRCS:.c=$(OBJEXT))


MAINOBJ = $(MAINSRC:.c=$(OBJEXT))

SRCS = $(ASRCS) $(CSRCS) $(MAINSRC)
OBJS = $(AOBJS) $(COBJS)

## MAINOBJ -> OBJFILES

all: clean default
$(info ${CSRCS})

%.o: %.c
	@$(CC)  $(CFLAGS) -c $< -o $@
	@echo "CC $<"

default: $(AOBJS) $(COBJS) $(MAINOBJ)
	$(CC) -o $(BIN) $(MAINOBJ) $(AOBJS) $(COBJS) $(LDFLAGS)

shared: $(AOBJS) $(COBJS) $(MAINOBJ)
	$(CC) -o liblvgl.so $(AOBJS) $(COBJS) $(LDFLAGS)

clean:
	rm -f $(BIN) $(AOBJS) $(COBJS) $(MAINOBJ)