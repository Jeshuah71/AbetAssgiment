import sys
from Algo_and_Struts_06_i_tree_node import TreeNode
from Tree_Algorithms import (
    numberOfLeaves,
    numberOfNodesWithASingleChild,
    numberOfNodesWithTwoChildren,
    numberOfNodesWithEvenDataItems,
    sumOfAllItems,
    printRuntimes,
)


already_printed_error = {}
def test(expected, given, test_name:str, t:TreeNode):
    """ Print the result of a test. """
    global already_printed_error
    if not test_name in already_printed_error:
        linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
        if expected == given:
            msg = "Test at line {0} ok.".format(linenum)
            # print(msg)
        else:
            msg = ("Test "+test_name+" at line {0} FAILED.".format(linenum))
            print(msg)
            print("\tExpected: "+ str(expected))
            print("\ttype: "+ str(type(expected)))
            print("\tGiven   : "+ str(given))
            print("\ttype: "+ str(type(given)))
            print("\tTester only prints a single error per section - there may be more")
            already_printed_error[test_name] = True
            print_graphvis_code(t)
def print_graphvis_code(t):
    print("digraph G {")
    _print_graphvis_code(t)
    print ("}")
def _print_graphvis_code(t:TreeNode):
    if(t.left_child):
        print ('"t'+str(t.key) + " v=" +str(t.value)+'"->"t'+str(t.left_child.key) + " v=" +str(t.left_child.value)+'"')
        _print_graphvis_code(t.left_child)
    if(t.right_child):
        print ('"t'+str(t.key) + " v=" +str(t.value)+'"->"t'+str(t.right_child.key) + " v=" +str(t.right_child.value)+'"')
        _print_graphvis_code(t.right_child)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    global already_printed_error
    print("Starting tests - only failed tests print unless you change that")
    #Add your tests here
def run_tests():
    print("Running additional tests...")

    # Test Case 1: Empty Tree case
    print("Test Case 1: Empty Tree")
    root = None
    assert numberOfLeaves(root) == 0, "Failed: numberOfLeaves for empty tree"
    assert numberOfNodesWithASingleChild(root) == 0, "Failed: numberOfNodesWithASingleChild for empty tree"
    assert numberOfNodesWithTwoChildren(root) == 0, "Failed: numberOfNodesWithTwoChildren for empty tree"
    assert numberOfNodesWithEvenDataItems(root) == 0, "Failed: numberOfNodesWithEvenDataItems for empty tree"
    assert sumOfAllItems(root) == 0, "Failed: sumOfAllItems for empty tree"

    # Test Case 2: Single Node Tree case
    print("Test Case 2: Single Node Tree")
    root = TreeNode(1, 10)  # Single node with value 10
    assert numberOfLeaves(root) == 1, "Failed: numberOfLeaves for single node tree"
    assert numberOfNodesWithASingleChild(root) == 0, "Failed: numberOfNodesWithASingleChild for single node tree"
    assert numberOfNodesWithTwoChildren(root) == 0, "Failed: numberOfNodesWithTwoChildren for single node tree"
    assert numberOfNodesWithEvenDataItems(root) == 1, "Failed: numberOfNodesWithEvenDataItems for single node tree"
    assert sumOfAllItems(root) == 10, "Failed: sumOfAllItems for single node tree"

    # Test Case 3: Full Binary Tree
    print("Test Case 3: Full Binary Tree")
    root = TreeNode(1, 4)
    root.left_child = TreeNode(2, 6)
    root.right_child = TreeNode(3, 8)
    root.left_child.left_child = TreeNode(4, 10)
    root.left_child.right_child = TreeNode(5, 12)
    root.right_child.left_child = TreeNode(6, 14)
    root.right_child.right_child = TreeNode(7, 16)
    assert numberOfLeaves(root) == 4, "Failed: numberOfLeaves for full binary tree"
    assert numberOfNodesWithASingleChild(root) == 0, "Failed: numberOfNodesWithASingleChild for full binary tree"
    assert numberOfNodesWithTwoChildren(root) == 3, "Failed: numberOfNodesWithTwoChildren for full binary tree"
    assert numberOfNodesWithEvenDataItems(root) == 7, "Failed: numberOfNodesWithEvenDataItems for full binary tree"
    assert sumOfAllItems(root) == 80, "Failed: sumOfAllItems for full binary tree"

    # Test Case 4: Skewed Tree (Left)
    print("Test Case 4: Skewed Tree (Left)")
    root = TreeNode(1, 10)
    root.left_child = TreeNode(2, 20)
    root.left_child.left_child = TreeNode(3, 30)
    root.left_child.left_child.left_child = TreeNode(4, 40)
    assert numberOfLeaves(root) == 1, "Failed: numberOfLeaves for skewed left tree"
    assert numberOfNodesWithASingleChild(root) == 3, "Failed: numberOfNodesWithASingleChild for skewed left tree"
    assert numberOfNodesWithTwoChildren(root) == 0, "Failed: numberOfNodesWithTwoChildren for skewed left tree"
    assert numberOfNodesWithEvenDataItems(root) == 4, "Failed: numberOfNodesWithEvenDataItems for skewed left tree"
    assert sumOfAllItems(root) == 100, "Failed: sumOfAllItems for skewed left tree"

    # Test Case 5: Skewed Tree (Right)
    print("Test Case 5: Skewed Tree (Right)")
    root = TreeNode(1, 5)
    root.right_child = TreeNode(2, 15)
    root.right_child.right_child = TreeNode(3, 25)
    root.right_child.right_child.right_child = TreeNode(4, 35)
    assert numberOfLeaves(root) == 1, "Failed: numberOfLeaves for skewed right tree"
    assert numberOfNodesWithASingleChild(root) == 3, "Failed: numberOfNodesWithASingleChild for skewed right tree"
    assert numberOfNodesWithTwoChildren(root) == 0, "Failed: numberOfNodesWithTwoChildren for skewed right tree"
    assert numberOfNodesWithEvenDataItems(root) == 0, "Failed: numberOfNodesWithEvenDataItems for skewed right tree"
    assert sumOfAllItems(root) == 80, "Failed: sumOfAllItems for skewed right tree"

    print("All additional tests passed successfully!")

    #Dr B's tests follow:
    print("Running tests for Tree Algorithms:")

    t0 = TreeNode( 0, 91 )#No Children
    t1 = TreeNode( 1, 36, left=t0 )#has left child
    t0.parent = t1

    t2 = TreeNode( 2, 7 )#No Children
    t3 = TreeNode( 3, 61, left=t2 )#has left child
    t2.parent = t3
    t4 = TreeNode( 4, 55, left=t1, right=t3 )#has two children
    t1.parent = t4
    t3.parent = t4

    t5 = TreeNode( 5, 51 )#No Children
    t6 = TreeNode( 6, 81 )#No Children
    t7 = TreeNode( 7, 9, left=t5, right=t6 )#has two children
    t5.parent = t7
    t6.parent = t7

    t8 = TreeNode( 8, 0 )#No Children
    t9 = TreeNode( 9, 55 )#No Children
    t10 = TreeNode( 10, 41, left=t8, right=t9 )#has two children
    t8.parent = t10
    t9.parent = t10
    t11 = TreeNode( 11, 39, left=t7, right=t10 )#has two children
    t7.parent = t11
    t10.parent = t11
    t12 = TreeNode( 12, 98, left=t4, right=t11 )#has two children
    t4.parent = t12
    t11.parent = t12


    t13 = TreeNode( 13, 47 )#No Children
    t14 = TreeNode( 14, 88, left=t13 )#has left child
    t13.parent = t14

    t15 = TreeNode( 15, 67 )#No Children
    t16 = TreeNode( 16, 6, right=t15 )#has right child
    t15.parent = t16
    t17 = TreeNode( 17, 63, left=t14, right=t16 )#has two children
    t14.parent = t17
    t16.parent = t17

    t18 = TreeNode( 18, 36 )#No Children
    t19 = TreeNode( 19, 36 )#No Children
    t20 = TreeNode( 20, 0, left=t18, right=t19 )#has two children
    t18.parent = t20
    t19.parent = t20

    t21 = TreeNode( 21, 6 )#No Children
    t22 = TreeNode( 22, 6 )#No Children
    t23 = TreeNode( 23, 6, left=t21, right=t22 )#has two children
    t21.parent = t23
    t22.parent = t23
    t24 = TreeNode( 24, 28, left=t20, right=t23 )#has two children
    t20.parent = t24
    t23.parent = t24
    t25 = TreeNode( 25, 80, left=t17, right=t24 )#has two children
    t17.parent = t25
    t24.parent = t25


    t26 = TreeNode( 26, 27 )#No Children
    t27 = TreeNode( 27, 31, left=t26 )#has left child
    t26.parent = t27

    t28 = TreeNode( 28, 3 )#No Children
    t29 = TreeNode( 29, 73 )#No Children
    t30 = TreeNode( 30, 46, left=t28, right=t29 )#has two children
    t28.parent = t30
    t29.parent = t30
    t31 = TreeNode( 31, 47, left=t27, right=t30 )#has two children
    t27.parent = t31
    t30.parent = t31

    t32 = TreeNode( 32, 25 )#No Children
    t33 = TreeNode( 33, 68 )#No Children
    t34 = TreeNode( 34, 41, left=t32, right=t33 )#has two children
    t32.parent = t34
    t33.parent = t34

    t35 = TreeNode( 35, 33 );#No Children
    t36 = TreeNode( 36, 93, left=t34, right=t35 )#has two children
    t34.parent = t36
    t35.parent = t36
    t37 = TreeNode( 37, 71, left=t31, right=t36 )#has two children
    t31.parent = t37
    t36.parent = t37


    t38 = TreeNode( 38, 57 )#No Children
    t39 = TreeNode( 39, 61, right=t38 )#has right child
    t38.parent = t39

    t40 = TreeNode( 40, 98 );#No Children
    t41 = TreeNode( 41, 62, left=t39, right=t40 )#has two children
    t39.parent = t41
    t40.parent = t41

    t42 = TreeNode( 42, 59 )#No Children
    t43 = TreeNode( 43, 30 )#No Children
    t44 = TreeNode( 44, 21, left=t42, right=t43 )#has two children
    t42.parent = t44
    t43.parent = t44

    t45 = TreeNode( 45, 0 )#No Children
    t46 = TreeNode( 46, 86 )#No Children
    t47 = TreeNode( 47, 20, left=t45, right=t46 )#has two children
    t45.parent = t47
    t46.parent = t47
    t48 = TreeNode( 48, 7, left=t44, right=t47 )#has two children
    t44.parent = t48
    t47.parent = t48
    t49 = TreeNode( 49, 42, left=t41, right=t48 )#has two children
    t41.parent = t49
    t48.parent = t49


    t50 = TreeNode( 50, 89 );#No Children

    t51 = TreeNode( 51, 3 )#No Children
    t52 = TreeNode( 52, 42, left=t51 )#has left child
    t51.parent = t52
    t53 = TreeNode( 53, 12, left=t50, right=t52 )#has two children
    t50.parent = t53
    t52.parent = t53

    t54 = TreeNode( 54, 38 )#No Children
    t55 = TreeNode( 55, 95, left=t54 )#has left child
    t54.parent = t55

    t56 = TreeNode( 56, 21 )#No Children
    t57 = TreeNode( 57, 75, right=t56 )#has right child
    t56.parent = t57
    t58 = TreeNode( 58, 5, left=t55, right=t57 )#has two children
    t55.parent = t58
    t57.parent = t58
    t59 = TreeNode( 59, 20, left=t53, right=t58 )#has two children
    t53.parent = t59
    t58.parent = t59


    t60 = TreeNode( 60, 31 )#No Children
    t61 = TreeNode( 61, 81, right=t60 )#has right child
    t60.parent = t61

    t62 = TreeNode( 62, 19 )#No Children
    t63 = TreeNode( 63, 58, right=t62 )#has right child
    t62.parent = t63
    t64 = TreeNode( 64, 93, left=t61, right=t63 )#has two children
    t61.parent = t64
    t63.parent = t64

    t65 = TreeNode( 65, 49 )#No Children
    t66 = TreeNode( 66, 44, left=t65 )#has left child
    t65.parent = t66

    t67 = TreeNode( 67, 33 );#No Children
    t68 = TreeNode( 68, 9, left=t66, right=t67 )#has two children
    t66.parent = t68
    t67.parent = t68
    t69 = TreeNode( 69, 5, left=t64, right=t68 )#has two children
    t64.parent = t69
    t68.parent = t69


    t70 = TreeNode( 70, 62 )#No Children
    t71 = TreeNode( 71, 22, left=t70 )#has left child
    t70.parent = t71

    t72 = TreeNode( 72, 55 )#No Children
    t73 = TreeNode( 73, 47, right=t72 )#has right child
    t72.parent = t73
    t74 = TreeNode( 74, 13, left=t71, right=t73 )#has two children
    t71.parent = t74
    t73.parent = t74

    t75 = TreeNode( 75, 33 );#No Children

    t76 = TreeNode( 76, 28 );#No Children
    t77 = TreeNode( 77, 55, left=t75, right=t76 )#has two children
    t75.parent = t77
    t76.parent = t77
    t78 = TreeNode( 78, 20, left=t74, right=t77 )#has two children
    t74.parent = t78
    t77.parent = t78


    t79 = TreeNode( 79, 86 )#No Children
    t80 = TreeNode( 80, 25 )#No Children
    t81 = TreeNode( 81, 18, left=t79, right=t80 )#has two children
    t79.parent = t81
    t80.parent = t81

    t82 = TreeNode( 82, 70 );#No Children
    t83 = TreeNode( 83, 16, left=t81, right=t82 )#has two children
    t81.parent = t83
    t82.parent = t83

    t84 = TreeNode( 84, 86 )#No Children
    t85 = TreeNode( 85, 73 )#No Children
    t86 = TreeNode( 86, 3, left=t84, right=t85 )#has two children
    t84.parent = t86
    t85.parent = t86

    t87 = TreeNode( 87, 6 );#No Children
    t88 = TreeNode( 88, 77, left=t86, right=t87 )#has two children
    t86.parent = t88
    t87.parent = t88
    t89 = TreeNode( 89, 3, left=t83, right=t88 )#has two children
    t83.parent = t89
    t88.parent = t89


    t90 = TreeNode( 90, 43 )#No Children
    t91 = TreeNode( 91, 95 )#No Children
    t92 = TreeNode( 92, 62, left=t90, right=t91 )#has two children
    t90.parent = t92
    t91.parent = t92

    t93 = TreeNode( 93, 80 );#No Children
    t94 = TreeNode( 94, 5, left=t92, right=t93 )#has two children
    t92.parent = t94
    t93.parent = t94

    t95 = TreeNode( 95, 87 )#No Children
    t96 = TreeNode( 96, 55, right=t95 )#has right child
    t95.parent = t96

    t97 = TreeNode( 97, 85 )#No Children
    t98 = TreeNode( 98, 38 )#No Children
    t99 = TreeNode( 99, 77, left=t97, right=t98 )#has two children
    t97.parent = t99
    t98.parent = t99
    t100 = TreeNode( 100, 54, left=t96, right=t99 )#has two children
    t96.parent = t100
    t99.parent = t100
    t101 = TreeNode( 101, 90, left=t94, right=t100 )#has two children
    t94.parent = t101
    t100.parent = t101


    t102 = TreeNode( 102, 23 )#No Children
    t103 = TreeNode( 103, 95 )#No Children
    t104 = TreeNode( 104, 93, left=t102, right=t103 )#has two children
    t102.parent = t104
    t103.parent = t104

    t105 = TreeNode( 105, 66 )#No Children
    t106 = TreeNode( 106, 98 )#No Children
    t107 = TreeNode( 107, 78, left=t105, right=t106 )#has two children
    t105.parent = t107
    t106.parent = t107
    t108 = TreeNode( 108, 53, left=t104, right=t107 )#has two children
    t104.parent = t108
    t107.parent = t108

    t109 = TreeNode( 109, 35 )#No Children
    t110 = TreeNode( 110, 2, left=t109 )#has left child
    t109.parent = t110

    t111 = TreeNode( 111, 85 )#No Children
    t112 = TreeNode( 112, 65, right=t111 )#has right child
    t111.parent = t112
    t113 = TreeNode( 113, 47, left=t110, right=t112 )#has two children
    t110.parent = t113
    t112.parent = t113
    t114 = TreeNode( 114, 29, left=t108, right=t113 )#has two children
    t108.parent = t114
    t113.parent = t114


    t115 = TreeNode( 115, 41 )#No Children
    t116 = TreeNode( 116, 77, left=t115 )#has left child
    t115.parent = t116

    t117 = TreeNode( 117, 63 )#No Children
    t118 = TreeNode( 118, 27, left=t117 )#has left child
    t117.parent = t118
    t119 = TreeNode( 119, 64, left=t116, right=t118 )#has two children
    t116.parent = t119
    t118.parent = t119

    t120 = TreeNode( 120, 65 )#No Children
    t121 = TreeNode( 121, 90, left=t120 )#has left child
    t120.parent = t121

    t122 = TreeNode( 122, 0 )#No Children
    t123 = TreeNode( 123, 48, left=t122 )#has left child
    t122.parent = t123
    t124 = TreeNode( 124, 67, left=t121, right=t123 )#has two children
    t121.parent = t124
    t123.parent = t124
    t125 = TreeNode( 125, 41, left=t119, right=t124 )#has two children
    t119.parent = t125
    t124.parent = t125

    t126 = TreeNode( 126, 53 )#No Children
    t127 = TreeNode( 127, 9 )#No Children
    t128 = TreeNode( 128, 92, left=t126, right=t127 )#has two children
    t126.parent = t128
    t127.parent = t128

    t129 = TreeNode( 129, 31 );#No Children
    t130 = TreeNode( 130, 29, left=t128, right=t129 )#has two children
    t128.parent = t130
    t129.parent = t130

    t131 = TreeNode( 131, 86 )#No Children
    t132 = TreeNode( 132, 40, right=t131 )#has right child
    t131.parent = t132

    t133 = TreeNode( 133, 56 )#No Children
    t134 = TreeNode( 134, 27 )#No Children
    t135 = TreeNode( 135, 70, left=t133, right=t134 )#has two children
    t133.parent = t135
    t134.parent = t135
    t136 = TreeNode( 136, 68, left=t132, right=t135 )#has two children
    t132.parent = t136
    t135.parent = t136
    t137 = TreeNode( 137, 44, left=t130, right=t136 )#has two children
    t130.parent = t137
    t136.parent = t137
    t138 = TreeNode( 138, 72, left=t125, right=t137 )#has two children
    t125.parent = t138
    t137.parent = t138

    t139 = TreeNode( 139, 25 )#No Children
    t140 = TreeNode( 140, 27 )#No Children
    t141 = TreeNode( 141, 53, left=t139, right=t140 )#has two children
    t139.parent = t141
    t140.parent = t141

    t142 = TreeNode( 142, 67 );#No Children
    t143 = TreeNode( 143, 88, left=t141, right=t142 )#has two children
    t141.parent = t143
    t142.parent = t143

    t144 = TreeNode( 144, 9 );#No Children

    t145 = TreeNode( 145, 69 )#No Children
    t146 = TreeNode( 146, 49 )#No Children
    t147 = TreeNode( 147, 74, left=t145, right=t146 )#has two children
    t145.parent = t147
    t146.parent = t147
    t148 = TreeNode( 148, 22, left=t144, right=t147 )#has two children
    t144.parent = t148
    t147.parent = t148
    t149 = TreeNode( 149, 39, left=t143, right=t148 )#has two children
    t143.parent = t149
    t148.parent = t149

    t150 = TreeNode( 150, 25 );#No Children

    t151 = TreeNode( 151, 63 );#No Children
    t152 = TreeNode( 152, 7, left=t150, right=t151 )#has two children
    t150.parent = t152
    t151.parent = t152

    t153 = TreeNode( 153, 85 )#No Children
    t154 = TreeNode( 154, 5, left=t153 )#has left child
    t153.parent = t154

    t155 = TreeNode( 155, 59 );#No Children
    t156 = TreeNode( 156, 8, left=t154, right=t155 )#has two children
    t154.parent = t156
    t155.parent = t156
    t157 = TreeNode( 157, 16, left=t152, right=t156 )#has two children
    t152.parent = t157
    t156.parent = t157
    t158 = TreeNode( 158, 14, left=t149, right=t157 )#has two children
    t149.parent = t158
    t157.parent = t158
    t159 = TreeNode( 159, 62, left=t138, right=t158 )#has two children
    t138.parent = t159
    t158.parent = t159


    t160 = TreeNode( 160, 12 );#No Children

    t161 = TreeNode( 161, 8 )#No Children
    t162 = TreeNode( 162, 27 )#No Children
    t163 = TreeNode( 163, 99, left=t161, right=t162 )#has two children
    t161.parent = t163
    t162.parent = t163
    t164 = TreeNode( 164, 69, left=t160, right=t163 )#has two children
    t160.parent = t164
    t163.parent = t164

    t165 = TreeNode( 165, 49 );#No Children

    t166 = TreeNode( 166, 12 )#No Children
    t167 = TreeNode( 167, 65, left=t166 )#has left child
    t166.parent = t167
    t168 = TreeNode( 168, 78, left=t165, right=t167 )#has two children
    t165.parent = t168
    t167.parent = t168
    t169 = TreeNode( 169, 52, left=t164, right=t168 )#has two children
    t164.parent = t169
    t168.parent = t169

    t170 = TreeNode( 170, 16 )#No Children
    t171 = TreeNode( 171, 85 )#No Children
    t172 = TreeNode( 172, 98, left=t170, right=t171 )#has two children
    t170.parent = t172
    t171.parent = t172

    t173 = TreeNode( 173, 62 )#No Children
    t174 = TreeNode( 174, 73, right=t173 )#has right child
    t173.parent = t174
    t175 = TreeNode( 175, 46, left=t172, right=t174 )#has two children
    t172.parent = t175
    t174.parent = t175

    t176 = TreeNode( 176, 66 )#No Children
    t177 = TreeNode( 177, 89 )#No Children
    t178 = TreeNode( 178, 18, left=t176, right=t177 )#has two children
    t176.parent = t178
    t177.parent = t178

    t179 = TreeNode( 179, 3 )#No Children
    t180 = TreeNode( 180, 33, right=t179 )#has right child
    t179.parent = t180
    t181 = TreeNode( 181, 57, left=t178, right=t180 )#has two children
    t178.parent = t181
    t180.parent = t181
    t182 = TreeNode( 182, 83, left=t175, right=t181 )#has two children
    t175.parent = t182
    t181.parent = t182
    t183 = TreeNode( 183, 96, left=t169, right=t182 )#has two children
    t169.parent = t183
    t182.parent = t183

    t184 = TreeNode( 184, 87 )#No Children
    t185 = TreeNode( 185, 64, right=t184 )#has right child
    t184.parent = t185

    t186 = TreeNode( 186, 79 )#No Children
    t187 = TreeNode( 187, 18 )#No Children
    t188 = TreeNode( 188, 58, left=t186, right=t187 )#has two children
    t186.parent = t188
    t187.parent = t188
    t189 = TreeNode( 189, 58, left=t185, right=t188 )#has two children
    t185.parent = t189
    t188.parent = t189

    t190 = TreeNode( 190, 3 )#No Children
    t191 = TreeNode( 191, 9, right=t190 )#has right child
    t190.parent = t191

    t192 = TreeNode( 192, 40 )#No Children
    t193 = TreeNode( 193, 1, left=t192 )#has left child
    t192.parent = t193
    t194 = TreeNode( 194, 62, left=t191, right=t193 )#has two children
    t191.parent = t194
    t193.parent = t194
    t195 = TreeNode( 195, 1, left=t189, right=t194 )#has two children
    t189.parent = t195
    t194.parent = t195

    t196 = TreeNode( 196, 63 )#No Children
    t197 = TreeNode( 197, 87, right=t196 )#has right child
    t196.parent = t197

    t198 = TreeNode( 198, 73 )#No Children
    t199 = TreeNode( 199, 14, right=t198 )#has right child
    t198.parent = t199
    t200 = TreeNode( 200, 43, left=t197, right=t199 )#has two children
    t197.parent = t200
    t199.parent = t200

    t201 = TreeNode( 201, 40 );#No Children

    t202 = TreeNode( 202, 95 )#No Children
    t203 = TreeNode( 203, 0 )#No Children
    t204 = TreeNode( 204, 85, left=t202, right=t203 )#has two children
    t202.parent = t204
    t203.parent = t204
    t205 = TreeNode( 205, 15, left=t201, right=t204 )#has two children
    t201.parent = t205
    t204.parent = t205
    t206 = TreeNode( 206, 95, left=t200, right=t205 )#has two children
    t200.parent = t206
    t205.parent = t206
    t207 = TreeNode( 207, 76, left=t195, right=t206 )#has two children
    t195.parent = t207
    t206.parent = t207
    t208 = TreeNode( 208, 31, left=t183, right=t207 )#has two children
    t183.parent = t208
    t207.parent = t208


    t209 = TreeNode( 209, 76 )#No Children
    t210 = TreeNode( 210, 84, left=t209 )#has left child
    t209.parent = t210

    t211 = TreeNode( 211, 43 )#No Children
    t212 = TreeNode( 212, 96, right=t211 )#has right child
    t211.parent = t212
    t213 = TreeNode( 213, 57, left=t210, right=t212 )#has two children
    t210.parent = t213
    t212.parent = t213

    t214 = TreeNode( 214, 30 );#No Children

    t215 = TreeNode( 215, 16 )#No Children
    t216 = TreeNode( 216, 15 )#No Children
    t217 = TreeNode( 217, 89, left=t215, right=t216 )#has two children
    t215.parent = t217
    t216.parent = t217
    t218 = TreeNode( 218, 89, left=t214, right=t217 )#has two children
    t214.parent = t218
    t217.parent = t218
    t219 = TreeNode( 219, 2, left=t213, right=t218 )#has two children
    t213.parent = t219
    t218.parent = t219

    t220 = TreeNode( 220, 0 )#No Children
    t221 = TreeNode( 221, 83, left=t220 )#has left child
    t220.parent = t221

    t222 = TreeNode( 222, 86 )#No Children
    t223 = TreeNode( 223, 40, left=t222 )#has left child
    t222.parent = t223
    t224 = TreeNode( 224, 20, left=t221, right=t223 )#has two children
    t221.parent = t224
    t223.parent = t224

    t225 = TreeNode( 225, 9 )#No Children
    t226 = TreeNode( 226, 80, right=t225 )#has right child
    t225.parent = t226

    t227 = TreeNode( 227, 50 )#No Children
    t228 = TreeNode( 228, 38 )#No Children
    t229 = TreeNode( 229, 86, left=t227, right=t228 )#has two children
    t227.parent = t229
    t228.parent = t229
    t230 = TreeNode( 230, 74, left=t226, right=t229 )#has two children
    t226.parent = t230
    t229.parent = t230
    t231 = TreeNode( 231, 33, left=t224, right=t230 )#has two children
    t224.parent = t231
    t230.parent = t231
    t232 = TreeNode( 232, 8, left=t219, right=t231 )#has two children
    t219.parent = t232
    t231.parent = t232

    t233 = TreeNode( 233, 64 );#No Children

    t234 = TreeNode( 234, 39 );#No Children
    t235 = TreeNode( 235, 48, left=t233, right=t234 )#has two children
    t233.parent = t235
    t234.parent = t235

    t236 = TreeNode( 236, 35 )#No Children
    t237 = TreeNode( 237, 94, right=t236 )#has right child
    t236.parent = t237

    t238 = TreeNode( 238, 27 )#No Children
    t239 = TreeNode( 239, 96, left=t238 )#has left child
    t238.parent = t239
    t240 = TreeNode( 240, 76, left=t237, right=t239 )#has two children
    t237.parent = t240
    t239.parent = t240
    t241 = TreeNode( 241, 55, left=t235, right=t240 )#has two children
    t235.parent = t241
    t240.parent = t241

    t242 = TreeNode( 242, 53 )#No Children
    t243 = TreeNode( 243, 22, right=t242 )#has right child
    t242.parent = t243

    t244 = TreeNode( 244, 90 )#No Children
    t245 = TreeNode( 245, 48 )#No Children
    t246 = TreeNode( 246, 46, left=t244, right=t245 )#has two children
    t244.parent = t246
    t245.parent = t246
    t247 = TreeNode( 247, 43, left=t243, right=t246 )#has two children
    t243.parent = t247
    t246.parent = t247

    t248 = TreeNode( 248, 42 )#No Children
    t249 = TreeNode( 249, 44 )#No Children
    t250 = TreeNode( 250, 85, left=t248, right=t249 )#has two children
    t248.parent = t250
    t249.parent = t250

    t251 = TreeNode( 251, 58 )#No Children
    t252 = TreeNode( 252, 21, left=t251 )#has left child
    t251.parent = t252
    t253 = TreeNode( 253, 16, left=t250, right=t252 )#has two children
    t250.parent = t253
    t252.parent = t253
    t254 = TreeNode( 254, 18, left=t247, right=t253 )#has two children
    t247.parent = t254
    t253.parent = t254
    t255 = TreeNode( 255, 83, left=t241, right=t254 )#has two children
    t241.parent = t255
    t254.parent = t255
    t256 = TreeNode( 256, 86, left=t232, right=t255 )#has two children
    t232.parent = t256
    t255.parent = t256


    t257 = TreeNode( 257, 36 )#No Children
    t258 = TreeNode( 258, 65, left=t257 )#has left child
    t257.parent = t258

    t259 = TreeNode( 259, 92 );#No Children
    t260 = TreeNode( 260, 82, left=t258, right=t259 )#has two children
    t258.parent = t260
    t259.parent = t260

    t261 = TreeNode( 261, 73 )#No Children
    t262 = TreeNode( 262, 39, right=t261 )#has right child
    t261.parent = t262

    t263 = TreeNode( 263, 8 )#No Children
    t264 = TreeNode( 264, 57, right=t263 )#has right child
    t263.parent = t264
    t265 = TreeNode( 265, 71, left=t262, right=t264 )#has two children
    t262.parent = t265
    t264.parent = t265
    t266 = TreeNode( 266, 13, left=t260, right=t265 )#has two children
    t260.parent = t266
    t265.parent = t266

    t267 = TreeNode( 267, 60 )#No Children
    t268 = TreeNode( 268, 32, left=t267 )#has left child
    t267.parent = t268

    t269 = TreeNode( 269, 97 )#No Children
    t270 = TreeNode( 270, 94 )#No Children
    t271 = TreeNode( 271, 49, left=t269, right=t270 )#has two children
    t269.parent = t271
    t270.parent = t271
    t272 = TreeNode( 272, 47, left=t268, right=t271 )#has two children
    t268.parent = t272
    t271.parent = t272

    t273 = TreeNode( 273, 68 );#No Children

    t274 = TreeNode( 274, 96 )#No Children
    t275 = TreeNode( 275, 77 )#No Children
    t276 = TreeNode( 276, 83, left=t274, right=t275 )#has two children
    t274.parent = t276
    t275.parent = t276
    t277 = TreeNode( 277, 99, left=t273, right=t276 )#has two children
    t273.parent = t277
    t276.parent = t277
    t278 = TreeNode( 278, 64, left=t272, right=t277 )#has two children
    t272.parent = t278
    t277.parent = t278
    t279 = TreeNode( 279, 54, left=t266, right=t278 )#has two children
    t266.parent = t279
    t278.parent = t279

    t280 = TreeNode( 280, 46 )#No Children
    t281 = TreeNode( 281, 17 )#No Children
    t282 = TreeNode( 282, 75, left=t280, right=t281 )#has two children
    t280.parent = t282
    t281.parent = t282

    t283 = TreeNode( 283, 96 )#No Children
    t284 = TreeNode( 284, 78 )#No Children
    t285 = TreeNode( 285, 33, left=t283, right=t284 )#has two children
    t283.parent = t285
    t284.parent = t285
    t286 = TreeNode( 286, 91, left=t282, right=t285 )#has two children
    t282.parent = t286
    t285.parent = t286

    t287 = TreeNode( 287, 77 )#No Children
    t288 = TreeNode( 288, 32, left=t287 )#has left child
    t287.parent = t288

    t289 = TreeNode( 289, 30 )#No Children
    t290 = TreeNode( 290, 25 )#No Children
    t291 = TreeNode( 291, 2, left=t289, right=t290 )#has two children
    t289.parent = t291
    t290.parent = t291
    t292 = TreeNode( 292, 21, left=t288, right=t291 )#has two children
    t288.parent = t292
    t291.parent = t292
    t293 = TreeNode( 293, 27, left=t286, right=t292 )#has two children
    t286.parent = t293
    t292.parent = t293

    t294 = TreeNode( 294, 76 )#No Children
    t295 = TreeNode( 295, 48, right=t294 )#has right child
    t294.parent = t295

    t296 = TreeNode( 296, 89 )#No Children
    t297 = TreeNode( 297, 96, left=t296 )#has left child
    t296.parent = t297
    t298 = TreeNode( 298, 96, left=t295, right=t297 )#has two children
    t295.parent = t298
    t297.parent = t298

    t299 = TreeNode( 299, 57 )#No Children
    t300 = TreeNode( 300, 84, right=t299 )#has right child
    t299.parent = t300

    t301 = TreeNode( 301, 11 )#No Children
    t302 = TreeNode( 302, 64, right=t301 )#has right child
    t301.parent = t302
    t303 = TreeNode( 303, 93, left=t300, right=t302 )#has two children
    t300.parent = t303
    t302.parent = t303
    t304 = TreeNode( 304, 25, left=t298, right=t303 )#has two children
    t298.parent = t304
    t303.parent = t304
    t305 = TreeNode( 305, 15, left=t293, right=t304 )#has two children
    t293.parent = t305
    t304.parent = t305
    t306 = TreeNode( 306, 79, left=t279, right=t305 )#has two children
    t279.parent = t306
    t305.parent = t306


    t307 = TreeNode( 307, 23 );#No Children

    t308 = TreeNode( 308, 38 );#No Children
    t309 = TreeNode( 309, 41, left=t307, right=t308 )#has two children
    t307.parent = t309
    t308.parent = t309

    t310 = TreeNode( 310, 88 )#No Children
    t311 = TreeNode( 311, 54, right=t310 )#has right child
    t310.parent = t311

    t312 = TreeNode( 312, 29 )#No Children
    t313 = TreeNode( 313, 34 )#No Children
    t314 = TreeNode( 314, 11, left=t312, right=t313 )#has two children
    t312.parent = t314
    t313.parent = t314
    t315 = TreeNode( 315, 66, left=t311, right=t314 )#has two children
    t311.parent = t315
    t314.parent = t315
    t316 = TreeNode( 316, 91, left=t309, right=t315 )#has two children
    t309.parent = t316
    t315.parent = t316

    t317 = TreeNode( 317, 42 )#No Children
    t318 = TreeNode( 318, 84 )#No Children
    t319 = TreeNode( 319, 88, left=t317, right=t318 )#has two children
    t317.parent = t319
    t318.parent = t319

    t320 = TreeNode( 320, 43 )#No Children
    t321 = TreeNode( 321, 47, right=t320 )#has right child
    t320.parent = t321
    t322 = TreeNode( 322, 60, left=t319, right=t321 )#has two children
    t319.parent = t322
    t321.parent = t322

    t323 = TreeNode( 323, 21 );#No Children

    t324 = TreeNode( 324, 17 )#No Children
    t325 = TreeNode( 325, 4 )#No Children
    t326 = TreeNode( 326, 2, left=t324, right=t325 )#has two children
    t324.parent = t326
    t325.parent = t326
    t327 = TreeNode( 327, 63, left=t323, right=t326 )#has two children
    t323.parent = t327
    t326.parent = t327
    t328 = TreeNode( 328, 17, left=t322, right=t327 )#has two children
    t322.parent = t328
    t327.parent = t328
    t329 = TreeNode( 329, 42, left=t316, right=t328 )#has two children
    t316.parent = t329
    t328.parent = t329

    t330 = TreeNode( 330, 50 )#No Children
    t331 = TreeNode( 331, 30, right=t330 )#has right child
    t330.parent = t331

    t332 = TreeNode( 332, 92 )#No Children
    t333 = TreeNode( 333, 24, left=t332 )#has left child
    t332.parent = t333
    t334 = TreeNode( 334, 13, left=t331, right=t333 )#has two children
    t331.parent = t334
    t333.parent = t334

    t335 = TreeNode( 335, 9 )#No Children
    t336 = TreeNode( 336, 60, right=t335 )#has right child
    t335.parent = t336

    t337 = TreeNode( 337, 52 );#No Children
    t338 = TreeNode( 338, 72, left=t336, right=t337 )#has two children
    t336.parent = t338
    t337.parent = t338
    t339 = TreeNode( 339, 45, left=t334, right=t338 )#has two children
    t334.parent = t339
    t338.parent = t339

    t340 = TreeNode( 340, 69 )#No Children
    t341 = TreeNode( 341, 41, left=t340 )#has left child
    t340.parent = t341

    t342 = TreeNode( 342, 72 );#No Children
    t343 = TreeNode( 343, 40, left=t341, right=t342 )#has two children
    t341.parent = t343
    t342.parent = t343

    t344 = TreeNode( 344, 27 )#No Children
    t345 = TreeNode( 345, 24, left=t344 )#has left child
    t344.parent = t345

    t346 = TreeNode( 346, 55 )#No Children
    t347 = TreeNode( 347, 96 )#No Children
    t348 = TreeNode( 348, 70, left=t346, right=t347 )#has two children
    t346.parent = t348
    t347.parent = t348
    t349 = TreeNode( 349, 20, left=t345, right=t348 )#has two children
    t345.parent = t349
    t348.parent = t349
    t350 = TreeNode( 350, 62, left=t343, right=t349 )#has two children
    t343.parent = t350
    t349.parent = t350
    t351 = TreeNode( 351, 84, left=t339, right=t350 )#has two children
    t339.parent = t351
    t350.parent = t351
    t352 = TreeNode( 352, 21, left=t329, right=t351 )#has two children
    t329.parent = t352
    t351.parent = t352


    t353 = TreeNode( 353, 98 )#No Children
    t354 = TreeNode( 354, 49, right=t353 )#has right child
    t353.parent = t354

    t355 = TreeNode( 355, 6 )#No Children
    t356 = TreeNode( 356, 11, right=t355 )#has right child
    t355.parent = t356
    t357 = TreeNode( 357, 70, left=t354, right=t356 )#has two children
    t354.parent = t357
    t356.parent = t357

    t358 = TreeNode( 358, 82 )#No Children
    t359 = TreeNode( 359, 84, right=t358 )#has right child
    t358.parent = t359

    t360 = TreeNode( 360, 74 );#No Children
    t361 = TreeNode( 361, 66, left=t359, right=t360 )#has two children
    t359.parent = t361
    t360.parent = t361
    t362 = TreeNode( 362, 61, left=t357, right=t361 )#has two children
    t357.parent = t362
    t361.parent = t362

    t363 = TreeNode( 363, 60 )#No Children
    t364 = TreeNode( 364, 16, left=t363 )#has left child
    t363.parent = t364

    t365 = TreeNode( 365, 80 )#No Children
    t366 = TreeNode( 366, 79 )#No Children
    t367 = TreeNode( 367, 43, left=t365, right=t366 )#has two children
    t365.parent = t367
    t366.parent = t367
    t368 = TreeNode( 368, 21, left=t364, right=t367 )#has two children
    t364.parent = t368
    t367.parent = t368

    t369 = TreeNode( 369, 17 )#No Children
    t370 = TreeNode( 370, 34 )#No Children
    t371 = TreeNode( 371, 42, left=t369, right=t370 )#has two children
    t369.parent = t371
    t370.parent = t371

    t372 = TreeNode( 372, 34 )#No Children
    t373 = TreeNode( 373, 5 )#No Children
    t374 = TreeNode( 374, 21, left=t372, right=t373 )#has two children
    t372.parent = t374
    t373.parent = t374
    t375 = TreeNode( 375, 49, left=t371, right=t374 )#has two children
    t371.parent = t375
    t374.parent = t375
    t376 = TreeNode( 376, 23, left=t368, right=t375 )#has two children
    t368.parent = t376
    t375.parent = t376
    t377 = TreeNode( 377, 85, left=t362, right=t376 )#has two children
    t362.parent = t377
    t376.parent = t377

    t378 = TreeNode( 378, 63 )#No Children
    t379 = TreeNode( 379, 56 )#No Children
    t380 = TreeNode( 380, 70, left=t378, right=t379 )#has two children
    t378.parent = t380
    t379.parent = t380

    t381 = TreeNode( 381, 93 )#No Children
    t382 = TreeNode( 382, 96, right=t381 )#has right child
    t381.parent = t382
    t383 = TreeNode( 383, 54, left=t380, right=t382 )#has two children
    t380.parent = t383
    t382.parent = t383

    t384 = TreeNode( 384, 71 )#No Children
    t385 = TreeNode( 385, 86, left=t384 )#has left child
    t384.parent = t385

    t386 = TreeNode( 386, 86 )#No Children
    t387 = TreeNode( 387, 30, right=t386 )#has right child
    t386.parent = t387
    t388 = TreeNode( 388, 40, left=t385, right=t387 )#has two children
    t385.parent = t388
    t387.parent = t388
    t389 = TreeNode( 389, 23, left=t383, right=t388 )#has two children
    t383.parent = t389
    t388.parent = t389

    t390 = TreeNode( 390, 64 );#No Children

    t391 = TreeNode( 391, 86 )#No Children
    t392 = TreeNode( 392, 39, right=t391 )#has right child
    t391.parent = t392
    t393 = TreeNode( 393, 13, left=t390, right=t392 )#has two children
    t390.parent = t393
    t392.parent = t393

    t394 = TreeNode( 394, 92 )#No Children
    t395 = TreeNode( 395, 66 )#No Children
    t396 = TreeNode( 396, 36, left=t394, right=t395 )#has two children
    t394.parent = t396
    t395.parent = t396

    t397 = TreeNode( 397, 87 )#No Children
    t398 = TreeNode( 398, 73, left=t397 )#has left child
    t397.parent = t398
    t399 = TreeNode( 399, 13, left=t396, right=t398 )#has two children
    t396.parent = t399
    t398.parent = t399
    t400 = TreeNode( 400, 46, left=t393, right=t399 )#has two children
    t393.parent = t400
    t399.parent = t400
    t401 = TreeNode( 401, 4, left=t389, right=t400 )#has two children
    t389.parent = t401
    t400.parent = t401
    t402 = TreeNode( 402, 26, left=t377, right=t401 )#has two children
    t377.parent = t402
    t401.parent = t402


    t403 = TreeNode( 403, 47 );#No Children

    t404 = TreeNode( 404, 16 );#No Children
    t405 = TreeNode( 405, 68, left=t403, right=t404 )#has two children
    t403.parent = t405
    t404.parent = t405

    t406 = TreeNode( 406, 21 )#No Children
    t407 = TreeNode( 407, 84, left=t406 )#has left child
    t406.parent = t407

    t408 = TreeNode( 408, 43 )#No Children
    t409 = TreeNode( 409, 21 )#No Children
    t410 = TreeNode( 410, 10, left=t408, right=t409 )#has two children
    t408.parent = t410
    t409.parent = t410
    t411 = TreeNode( 411, 7, left=t407, right=t410 )#has two children
    t407.parent = t411
    t410.parent = t411
    t412 = TreeNode( 412, 88, left=t405, right=t411 )#has two children
    t405.parent = t412
    t411.parent = t412

    t413 = TreeNode( 413, 27 );#No Children

    t414 = TreeNode( 414, 81 )#No Children
    t415 = TreeNode( 415, 19, left=t414 )#has left child
    t414.parent = t415
    t416 = TreeNode( 416, 88, left=t413, right=t415 )#has two children
    t413.parent = t416
    t415.parent = t416

    t417 = TreeNode( 417, 65 );#No Children

    t418 = TreeNode( 418, 17 )#No Children
    t419 = TreeNode( 419, 29, left=t418 )#has left child
    t418.parent = t419
    t420 = TreeNode( 420, 52, left=t417, right=t419 )#has two children
    t417.parent = t420
    t419.parent = t420
    t421 = TreeNode( 421, 14, left=t416, right=t420 )#has two children
    t416.parent = t421
    t420.parent = t421
    t422 = TreeNode( 422, 56, left=t412, right=t421 )#has two children
    t412.parent = t422
    t421.parent = t422

    t423 = TreeNode( 423, 17 );#No Children

    t424 = TreeNode( 424, 27 )#No Children
    t425 = TreeNode( 425, 84, right=t424 )#has right child
    t424.parent = t425
    t426 = TreeNode( 426, 65, left=t423, right=t425 )#has two children
    t423.parent = t426
    t425.parent = t426

    t427 = TreeNode( 427, 27 )#No Children
    t428 = TreeNode( 428, 92 )#No Children
    t429 = TreeNode( 429, 43, left=t427, right=t428 )#has two children
    t427.parent = t429
    t428.parent = t429

    t430 = TreeNode( 430, 22 )#No Children
    t431 = TreeNode( 431, 91, left=t430 )#has left child
    t430.parent = t431
    t432 = TreeNode( 432, 31, left=t429, right=t431 )#has two children
    t429.parent = t432
    t431.parent = t432
    t433 = TreeNode( 433, 90, left=t426, right=t432 )#has two children
    t426.parent = t433
    t432.parent = t433

    t434 = TreeNode( 434, 95 );#No Children

    t435 = TreeNode( 435, 84 );#No Children
    t436 = TreeNode( 436, 2, left=t434, right=t435 )#has two children
    t434.parent = t436
    t435.parent = t436

    t437 = TreeNode( 437, 37 )#No Children
    t438 = TreeNode( 438, 37, left=t437 )#has left child
    t437.parent = t438

    t439 = TreeNode( 439, 14 )#No Children
    t440 = TreeNode( 440, 60 )#No Children
    t441 = TreeNode( 441, 87, left=t439, right=t440 )#has two children
    t439.parent = t441
    t440.parent = t441
    t442 = TreeNode( 442, 6, left=t438, right=t441 )#has two children
    t438.parent = t442
    t441.parent = t442
    t443 = TreeNode( 443, 71, left=t436, right=t442 )#has two children
    t436.parent = t443
    t442.parent = t443
    t444 = TreeNode( 444, 53, left=t433, right=t443 )#has two children
    t433.parent = t444
    t443.parent = t444
    t445 = TreeNode( 445, 43, left=t422, right=t444 )#has two children
    t422.parent = t445
    t444.parent = t445


    t446 = TreeNode( 446, 4 );#No Children

    t447 = TreeNode( 447, 44 );#No Children
    t448 = TreeNode( 448, 74, left=t446, right=t447 )#has two children
    t446.parent = t448
    t447.parent = t448

    t449 = TreeNode( 449, 17 )#No Children
    t450 = TreeNode( 450, 7, left=t449 )#has left child
    t449.parent = t450

    t451 = TreeNode( 451, 22 );#No Children
    t452 = TreeNode( 452, 97, left=t450, right=t451 )#has two children
    t450.parent = t452
    t451.parent = t452
    t453 = TreeNode( 453, 71, left=t448, right=t452 )#has two children
    t448.parent = t453
    t452.parent = t453

    t454 = TreeNode( 454, 59 )#No Children
    t455 = TreeNode( 455, 64, right=t454 )#has right child
    t454.parent = t455

    t456 = TreeNode( 456, 79 )#No Children
    t457 = TreeNode( 457, 3 )#No Children
    t458 = TreeNode( 458, 45, left=t456, right=t457 )#has two children
    t456.parent = t458
    t457.parent = t458
    t459 = TreeNode( 459, 98, left=t455, right=t458 )#has two children
    t455.parent = t459
    t458.parent = t459

    t460 = TreeNode( 460, 86 )#No Children
    t461 = TreeNode( 461, 89, left=t460 )#has left child
    t460.parent = t461

    t462 = TreeNode( 462, 6 );#No Children
    t463 = TreeNode( 463, 46, left=t461, right=t462 )#has two children
    t461.parent = t463
    t462.parent = t463
    t464 = TreeNode( 464, 48, left=t459, right=t463 )#has two children
    t459.parent = t464
    t463.parent = t464
    t465 = TreeNode( 465, 19, left=t453, right=t464 )#has two children
    t453.parent = t465
    t464.parent = t465

    t466 = TreeNode( 466, 5 );#No Children

    t467 = TreeNode( 467, 48 )#No Children
    t468 = TreeNode( 468, 15 )#No Children
    t469 = TreeNode( 469, 33, left=t467, right=t468 )#has two children
    t467.parent = t469
    t468.parent = t469
    t470 = TreeNode( 470, 17, left=t466, right=t469 )#has two children
    t466.parent = t470
    t469.parent = t470

    t471 = TreeNode( 471, 42 );#No Children

    t472 = TreeNode( 472, 68 )#No Children
    t473 = TreeNode( 473, 22 )#No Children
    t474 = TreeNode( 474, 5, left=t472, right=t473 )#has two children
    t472.parent = t474
    t473.parent = t474
    t475 = TreeNode( 475, 60, left=t471, right=t474 )#has two children
    t471.parent = t475
    t474.parent = t475
    t476 = TreeNode( 476, 28, left=t470, right=t475 )#has two children
    t470.parent = t476
    t475.parent = t476

    t477 = TreeNode( 477, 97 )#No Children
    t478 = TreeNode( 478, 38, left=t477 )#has left child
    t477.parent = t478

    t479 = TreeNode( 479, 51 )#No Children
    t480 = TreeNode( 480, 30, left=t479 )#has left child
    t479.parent = t480
    t481 = TreeNode( 481, 48, left=t478, right=t480 )#has two children
    t478.parent = t481
    t480.parent = t481

    t482 = TreeNode( 482, 88 )#No Children
    t483 = TreeNode( 483, 24, right=t482 )#has right child
    t482.parent = t483

    t484 = TreeNode( 484, 84 )#No Children
    t485 = TreeNode( 485, 56, left=t484 )#has left child
    t484.parent = t485
    t486 = TreeNode( 486, 75, left=t483, right=t485 )#has two children
    t483.parent = t486
    t485.parent = t486
    t487 = TreeNode( 487, 94, left=t481, right=t486 )#has two children
    t481.parent = t487
    t486.parent = t487
    t488 = TreeNode( 488, 42, left=t476, right=t487 )#has two children
    t476.parent = t488
    t487.parent = t488
    t489 = TreeNode( 489, 25, left=t465, right=t488 )#has two children
    t465.parent = t489
    t488.parent = t489


    t490 = TreeNode( 490, 93 )#No Children
    t491 = TreeNode( 491, 80 )#No Children
    t492 = TreeNode( 492, 89, left=t490, right=t491 )#has two children
    t490.parent = t492
    t491.parent = t492

    t493 = TreeNode( 493, 56 )#No Children
    t494 = TreeNode( 494, 6 )#No Children
    t495 = TreeNode( 495, 26, left=t493, right=t494 )#has two children
    t493.parent = t495
    t494.parent = t495
    t496 = TreeNode( 496, 4, left=t492, right=t495 )#has two children
    t492.parent = t496
    t495.parent = t496

    t497 = TreeNode( 497, 84 )#No Children
    t498 = TreeNode( 498, 70 )#No Children
    t499 = TreeNode( 499, 35, left=t497, right=t498 )#has two children
    t497.parent = t499
    t498.parent = t499

    t500 = TreeNode( 500, 47 )#No Children
    t501 = TreeNode( 501, 12 )#No Children
    t502 = TreeNode( 502, 93, left=t500, right=t501 )#has two children
    t500.parent = t502
    t501.parent = t502
    t503 = TreeNode( 503, 41, left=t499, right=t502 )#has two children
    t499.parent = t503
    t502.parent = t503
    t504 = TreeNode( 504, 53, left=t496, right=t503 )#has two children
    t496.parent = t504
    t503.parent = t504

    t505 = TreeNode( 505, 22 )#No Children
    t506 = TreeNode( 506, 62, right=t505 )#has right child
    t505.parent = t506

    t507 = TreeNode( 507, 75 )#No Children
    t508 = TreeNode( 508, 98 )#No Children
    t509 = TreeNode( 509, 95, left=t507, right=t508 )#has two children
    t507.parent = t509
    t508.parent = t509
    t510 = TreeNode( 510, 29, left=t506, right=t509 )#has two children
    t506.parent = t510
    t509.parent = t510

    t511 = TreeNode( 511, 16 );#No Children

    t512 = TreeNode( 512, 94 );#No Children
    t513 = TreeNode( 513, 51, left=t511, right=t512 )#has two children
    t511.parent = t513
    t512.parent = t513
    t514 = TreeNode( 514, 4, left=t510, right=t513 )#has two children
    t510.parent = t514
    t513.parent = t514
    t515 = TreeNode( 515, 21, left=t504, right=t514 )#has two children
    t504.parent = t515
    t514.parent = t515

    t516 = TreeNode( 516, 94 )#No Children
    t517 = TreeNode( 517, 78, right=t516 )#has right child
    t516.parent = t517

    t518 = TreeNode( 518, 82 )#No Children
    t519 = TreeNode( 519, 65 )#No Children
    t520 = TreeNode( 520, 1, left=t518, right=t519 )#has two children
    t518.parent = t520
    t519.parent = t520
    t521 = TreeNode( 521, 1, left=t517, right=t520 )#has two children
    t517.parent = t521
    t520.parent = t521

    t522 = TreeNode( 522, 50 );#No Children

    t523 = TreeNode( 523, 48 )#No Children
    t524 = TreeNode( 524, 5, right=t523 )#has right child
    t523.parent = t524
    t525 = TreeNode( 525, 25, left=t522, right=t524 )#has two children
    t522.parent = t525
    t524.parent = t525
    t526 = TreeNode( 526, 33, left=t521, right=t525 )#has two children
    t521.parent = t526
    t525.parent = t526

    t527 = TreeNode( 527, 72 )#No Children
    t528 = TreeNode( 528, 85, right=t527 )#has right child
    t527.parent = t528

    t529 = TreeNode( 529, 77 );#No Children
    t530 = TreeNode( 530, 98, left=t528, right=t529 )#has two children
    t528.parent = t530
    t529.parent = t530

    t531 = TreeNode( 531, 31 )#No Children
    t532 = TreeNode( 532, 39 )#No Children
    t533 = TreeNode( 533, 20, left=t531, right=t532 )#has two children
    t531.parent = t533
    t532.parent = t533

    t534 = TreeNode( 534, 63 );#No Children
    t535 = TreeNode( 535, 82, left=t533, right=t534 )#has two children
    t533.parent = t535
    t534.parent = t535
    t536 = TreeNode( 536, 50, left=t530, right=t535 )#has two children
    t530.parent = t536
    t535.parent = t536
    t537 = TreeNode( 537, 49, left=t526, right=t536 )#has two children
    t526.parent = t537
    t536.parent = t537
    t538 = TreeNode( 538, 28, left=t515, right=t537 )#has two children
    t515.parent = t538
    t537.parent = t538


    t539 = TreeNode( 539, 13 )#No Children
    t540 = TreeNode( 540, 58 )#No Children
    t541 = TreeNode( 541, 86, left=t539, right=t540 )#has two children
    t539.parent = t541
    t540.parent = t541

    t542 = TreeNode( 542, 25 )#No Children
    t543 = TreeNode( 543, 58, left=t542 )#has left child
    t542.parent = t543
    t544 = TreeNode( 544, 56, left=t541, right=t543 )#has two children
    t541.parent = t544
    t543.parent = t544

    t545 = TreeNode( 545, 31 )#No Children
    t546 = TreeNode( 546, 62, left=t545 )#has left child
    t545.parent = t546

    t547 = TreeNode( 547, 88 );#No Children
    t548 = TreeNode( 548, 96, left=t546, right=t547 )#has two children
    t546.parent = t548
    t547.parent = t548
    t549 = TreeNode( 549, 65, left=t544, right=t548 )#has two children
    t544.parent = t549
    t548.parent = t549

    t550 = TreeNode( 550, 45 )#No Children
    t551 = TreeNode( 551, 66, left=t550 )#has left child
    t550.parent = t551

    t552 = TreeNode( 552, 56 )#No Children
    t553 = TreeNode( 553, 52, left=t552 )#has left child
    t552.parent = t553
    t554 = TreeNode( 554, 61, left=t551, right=t553 )#has two children
    t551.parent = t554
    t553.parent = t554

    t555 = TreeNode( 555, 89 )#No Children
    t556 = TreeNode( 556, 16 )#No Children
    t557 = TreeNode( 557, 55, left=t555, right=t556 )#has two children
    t555.parent = t557
    t556.parent = t557

    t558 = TreeNode( 558, 59 )#No Children
    t559 = TreeNode( 559, 97, left=t558 )#has left child
    t558.parent = t559
    t560 = TreeNode( 560, 11, left=t557, right=t559 )#has two children
    t557.parent = t560
    t559.parent = t560
    t561 = TreeNode( 561, 22, left=t554, right=t560 )#has two children
    t554.parent = t561
    t560.parent = t561
    t562 = TreeNode( 562, 59, left=t549, right=t561 )#has two children
    t549.parent = t562
    t561.parent = t562

    t563 = TreeNode( 563, 89 )#No Children
    t564 = TreeNode( 564, 68, right=t563 )#has right child
    t563.parent = t564

    t565 = TreeNode( 565, 51 );#No Children
    t566 = TreeNode( 566, 36, left=t564, right=t565 )#has two children
    t564.parent = t566
    t565.parent = t566

    t567 = TreeNode( 567, 30 )#No Children
    t568 = TreeNode( 568, 43, left=t567 )#has left child
    t567.parent = t568

    t569 = TreeNode( 569, 61 )#No Children
    t570 = TreeNode( 570, 11 )#No Children
    t571 = TreeNode( 571, 28, left=t569, right=t570 )#has two children
    t569.parent = t571
    t570.parent = t571
    t572 = TreeNode( 572, 91, left=t568, right=t571 )#has two children
    t568.parent = t572
    t571.parent = t572
    t573 = TreeNode( 573, 96, left=t566, right=t572 )#has two children
    t566.parent = t573
    t572.parent = t573

    t574 = TreeNode( 574, 55 )#No Children
    t575 = TreeNode( 575, 15, left=t574 )#has left child
    t574.parent = t575

    t576 = TreeNode( 576, 97 )#No Children
    t577 = TreeNode( 577, 32, right=t576 )#has right child
    t576.parent = t577
    t578 = TreeNode( 578, 22, left=t575, right=t577 )#has two children
    t575.parent = t578
    t577.parent = t578

    t579 = TreeNode( 579, 10 )#No Children
    t580 = TreeNode( 580, 14 )#No Children
    t581 = TreeNode( 581, 27, left=t579, right=t580 )#has two children
    t579.parent = t581
    t580.parent = t581

    t582 = TreeNode( 582, 65 )#No Children
    t583 = TreeNode( 583, 22 )#No Children
    t584 = TreeNode( 584, 98, left=t582, right=t583 )#has two children
    t582.parent = t584
    t583.parent = t584
    t585 = TreeNode( 585, 71, left=t581, right=t584 )#has two children
    t581.parent = t585
    t584.parent = t585
    t586 = TreeNode( 586, 44, left=t578, right=t585 )#has two children
    t578.parent = t586
    t585.parent = t586
    t587 = TreeNode( 587, 93, left=t573, right=t586 )#has two children
    t573.parent = t587
    t586.parent = t587
    t588 = TreeNode( 588, 16, left=t562, right=t587 )#has two children
    t562.parent = t588
    t587.parent = t588

    print('Tests for numberOfLeaves')
    test(6, numberOfLeaves(t12), 'numberOfLeaves', t12)
    test(6, numberOfLeaves(t25), 'numberOfLeaves', t25)
    test(6, numberOfLeaves(t37), 'numberOfLeaves', t37)
    test(6, numberOfLeaves(t49), 'numberOfLeaves', t49)
    test(4, numberOfLeaves(t59), 'numberOfLeaves', t59)
    test(4, numberOfLeaves(t69), 'numberOfLeaves', t69)
    test(4, numberOfLeaves(t78), 'numberOfLeaves', t78)
    test(6, numberOfLeaves(t89), 'numberOfLeaves', t89)
    test(6, numberOfLeaves(t101), 'numberOfLeaves', t101)
    test(6, numberOfLeaves(t114), 'numberOfLeaves', t114)
    test(20, numberOfLeaves(t159), 'numberOfLeaves', t159)
    test(21, numberOfLeaves(t208), 'numberOfLeaves', t208)
    test(20, numberOfLeaves(t256), 'numberOfLeaves', t256)
    test(21, numberOfLeaves(t306), 'numberOfLeaves', t306)
    test(20, numberOfLeaves(t352), 'numberOfLeaves', t352)
    test(21, numberOfLeaves(t402), 'numberOfLeaves', t402)
    test(19, numberOfLeaves(t445), 'numberOfLeaves', t445)
    test(19, numberOfLeaves(t489), 'numberOfLeaves', t489)
    test(23, numberOfLeaves(t538), 'numberOfLeaves', t538)
    test(21, numberOfLeaves(t588), 'numberOfLeaves', t588)
    print('Tests for numberOfNodesWithASingleChild')
    test(2, numberOfNodesWithASingleChild(t12), 'numberOfNodesWithASingleChild', t12)
    test(2, numberOfNodesWithASingleChild(t25), 'numberOfNodesWithASingleChild', t25)
    test(1, numberOfNodesWithASingleChild(t37), 'numberOfNodesWithASingleChild', t37)
    test(1, numberOfNodesWithASingleChild(t49), 'numberOfNodesWithASingleChild', t49)
    test(3, numberOfNodesWithASingleChild(t59), 'numberOfNodesWithASingleChild', t59)
    test(3, numberOfNodesWithASingleChild(t69), 'numberOfNodesWithASingleChild', t69)
    test(2, numberOfNodesWithASingleChild(t78), 'numberOfNodesWithASingleChild', t78)
    test(0, numberOfNodesWithASingleChild(t89), 'numberOfNodesWithASingleChild', t89)
    test(1, numberOfNodesWithASingleChild(t101), 'numberOfNodesWithASingleChild', t101)
    test(2, numberOfNodesWithASingleChild(t114), 'numberOfNodesWithASingleChild', t114)
    test(6, numberOfNodesWithASingleChild(t159), 'numberOfNodesWithASingleChild', t159)
    test(8, numberOfNodesWithASingleChild(t208), 'numberOfNodesWithASingleChild', t208)
    test(9, numberOfNodesWithASingleChild(t256), 'numberOfNodesWithASingleChild', t256)
    test(9, numberOfNodesWithASingleChild(t306), 'numberOfNodesWithASingleChild', t306)
    test(7, numberOfNodesWithASingleChild(t352), 'numberOfNodesWithASingleChild', t352)
    test(9, numberOfNodesWithASingleChild(t402), 'numberOfNodesWithASingleChild', t402)
    test(6, numberOfNodesWithASingleChild(t445), 'numberOfNodesWithASingleChild', t445)
    test(7, numberOfNodesWithASingleChild(t489), 'numberOfNodesWithASingleChild', t489)
    test(4, numberOfNodesWithASingleChild(t538), 'numberOfNodesWithASingleChild', t538)
    test(9, numberOfNodesWithASingleChild(t588), 'numberOfNodesWithASingleChild', t588)
    print('Tests for numberOfNodesWithTwoChildren')
    test(5, numberOfNodesWithTwoChildren(t12), 'numberOfNodesWithTwoChildren', t12)
    test(5, numberOfNodesWithTwoChildren(t25), 'numberOfNodesWithTwoChildren', t25)
    test(5, numberOfNodesWithTwoChildren(t37), 'numberOfNodesWithTwoChildren', t37)
    test(5, numberOfNodesWithTwoChildren(t49), 'numberOfNodesWithTwoChildren', t49)
    test(3, numberOfNodesWithTwoChildren(t59), 'numberOfNodesWithTwoChildren', t59)
    test(3, numberOfNodesWithTwoChildren(t69), 'numberOfNodesWithTwoChildren', t69)
    test(3, numberOfNodesWithTwoChildren(t78), 'numberOfNodesWithTwoChildren', t78)
    test(5, numberOfNodesWithTwoChildren(t89), 'numberOfNodesWithTwoChildren', t89)
    test(5, numberOfNodesWithTwoChildren(t101), 'numberOfNodesWithTwoChildren', t101)
    test(5, numberOfNodesWithTwoChildren(t114), 'numberOfNodesWithTwoChildren', t114)
    test(19, numberOfNodesWithTwoChildren(t159), 'numberOfNodesWithTwoChildren', t159)
    test(20, numberOfNodesWithTwoChildren(t208), 'numberOfNodesWithTwoChildren', t208)
    test(19, numberOfNodesWithTwoChildren(t256), 'numberOfNodesWithTwoChildren', t256)
    test(20, numberOfNodesWithTwoChildren(t306), 'numberOfNodesWithTwoChildren', t306)
    test(19, numberOfNodesWithTwoChildren(t352), 'numberOfNodesWithTwoChildren', t352)
    test(20, numberOfNodesWithTwoChildren(t402), 'numberOfNodesWithTwoChildren', t402)
    test(18, numberOfNodesWithTwoChildren(t445), 'numberOfNodesWithTwoChildren', t445)
    test(18, numberOfNodesWithTwoChildren(t489), 'numberOfNodesWithTwoChildren', t489)
    test(22, numberOfNodesWithTwoChildren(t538), 'numberOfNodesWithTwoChildren', t538)
    test(20, numberOfNodesWithTwoChildren(t588), 'numberOfNodesWithTwoChildren', t588)
    print('Tests for numberOfNodesWithEvenDataItems')
    test(3, numberOfNodesWithEvenDataItems(t12), 'numberOfNodesWithEvenDataItems', t12)
    test(10, numberOfNodesWithEvenDataItems(t25), 'numberOfNodesWithEvenDataItems', t25)
    test(2, numberOfNodesWithEvenDataItems(t37), 'numberOfNodesWithEvenDataItems', t37)
    test(7, numberOfNodesWithEvenDataItems(t49), 'numberOfNodesWithEvenDataItems', t49)
    test(4, numberOfNodesWithEvenDataItems(t59), 'numberOfNodesWithEvenDataItems', t59)
    test(2, numberOfNodesWithEvenDataItems(t69), 'numberOfNodesWithEvenDataItems', t69)
    test(4, numberOfNodesWithEvenDataItems(t78), 'numberOfNodesWithEvenDataItems', t78)
    test(6, numberOfNodesWithEvenDataItems(t89), 'numberOfNodesWithEvenDataItems', t89)
    test(5, numberOfNodesWithEvenDataItems(t101), 'numberOfNodesWithEvenDataItems', t101)
    test(4, numberOfNodesWithEvenDataItems(t114), 'numberOfNodesWithEvenDataItems', t114)
    test(19, numberOfNodesWithEvenDataItems(t159), 'numberOfNodesWithEvenDataItems', t159)
    test(22, numberOfNodesWithEvenDataItems(t208), 'numberOfNodesWithEvenDataItems', t208)
    test(31, numberOfNodesWithEvenDataItems(t256), 'numberOfNodesWithEvenDataItems', t256)
    test(23, numberOfNodesWithEvenDataItems(t306), 'numberOfNodesWithEvenDataItems', t306)
    test(27, numberOfNodesWithEvenDataItems(t352), 'numberOfNodesWithEvenDataItems', t352)
    test(29, numberOfNodesWithEvenDataItems(t402), 'numberOfNodesWithEvenDataItems', t402)
    test(18, numberOfNodesWithEvenDataItems(t445), 'numberOfNodesWithEvenDataItems', t445)
    test(25, numberOfNodesWithEvenDataItems(t489), 'numberOfNodesWithEvenDataItems', t489)
    test(25, numberOfNodesWithEvenDataItems(t538), 'numberOfNodesWithEvenDataItems', t538)
    test(25, numberOfNodesWithEvenDataItems(t588), 'numberOfNodesWithEvenDataItems', t588)
    print('Tests for sumOfAllItems')
    test(624, sumOfAllItems(t12), 'sumOfAllItems', t12)
    test(469, sumOfAllItems(t25), 'sumOfAllItems', t25)
    test(558, sumOfAllItems(t37), 'sumOfAllItems', t37)
    test(543, sumOfAllItems(t49), 'sumOfAllItems', t49)
    test(400, sumOfAllItems(t59), 'sumOfAllItems', t59)
    test(422, sumOfAllItems(t69), 'sumOfAllItems', t69)
    test(335, sumOfAllItems(t78), 'sumOfAllItems', t78)
    test(463, sumOfAllItems(t89), 'sumOfAllItems', t89)
    test(771, sumOfAllItems(t101), 'sumOfAllItems', t101)
    test(769, sumOfAllItems(t114), 'sumOfAllItems', t114)
    test(2126, sumOfAllItems(t159), 'sumOfAllItems', t159)
    test(2493, sumOfAllItems(t208), 'sumOfAllItems', t208)
    test(2493, sumOfAllItems(t256), 'sumOfAllItems', t256)
    test(2939, sumOfAllItems(t306), 'sumOfAllItems', t306)
    test(2133, sumOfAllItems(t352), 'sumOfAllItems', t352)
    test(2623, sumOfAllItems(t402), 'sumOfAllItems', t402)
    test(2031, sumOfAllItems(t445), 'sumOfAllItems', t445)
    test(2073, sumOfAllItems(t489), 'sumOfAllItems', t489)
    test(2532, sumOfAllItems(t538), 'sumOfAllItems', t538)
    test(2611, sumOfAllItems(t588), 'sumOfAllItems', t588)
    printRuntimes()
    print("Ending tests")

test_suite()
