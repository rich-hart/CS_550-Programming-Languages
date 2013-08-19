pager = more
PART_1_1 = ./Part_1_1/AssignmentPart1_1.py
PART_1_2 = ./Part_1_2/AssignmentPart1_2.py
PART_2_1 = ./Part_2_1/AssignmentPart2_1.java
PART_2_2 = ./Part_2_2/AssignmentPart2_2.java
PYTHON_CC = python
JAVAC=javac
JAVA=java


view-rdp_1_1: PART_1_1
	-$(pager) $(PART_1_1)

run-rdp_1_1: PART_1_1
	$(PYTHON_CC) $(PART_1_1)

view-rdp_1_2: PART_1_2
	-$(pager) $(PART_1_2)

run-rdp_1_2: PART_1_2
	$(PYTHON_CC) $(PART_1_2)

view-rdp_2_1: PART_2_1
	-$(pager) $(PART_2_1)

run-rdp_2_1: java_exe_part_2_1
	$(JAVA) -classpath $(dir $(PART_2_1)) $(basename $(notdir $(PART_2_1)))

java_exe_part_2_1: PART_2_1
	$(JAVAC) $(PART_2_1)

view-rdp_2_2: 
	-$(pager) ./Part_2_2/cup/Parser.cup

run-rdp_2_2: 
	ant -buildfile ./Part_2_2/build.xml run

clean: 
	ant -buildfile ./Part_2_2/build.xml clean



