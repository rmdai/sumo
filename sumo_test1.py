# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 09:42:24 2020

@author: 86189
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:19:33 2019

@author: 86189
"""

import os
import lxml.html
etree=lxml.html.etree



sumo_file_folder = "C:/Users/86189/Desktop/构建高速路段/"
lane_width = 3.5

filename_prefix = "C:/Users/86189/Desktop/构建高速路段/ArterialIntersection."

def Generate_edge_elements_approach(filename = sumo_file_folder  + 'ArterialIntersection.edg.xml',x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100,vf = 120,offset_x = 0,offset_y = 0,lane_width = 3.5):
        """
        Change the net etree element. and return edges and lanes, both are dict. Each value is a etree element. 
        
        Note that this function only generate the elements for single approach.
        ---------------------------------------------------
        Output: edges
                lanes
        """
        net = etree.Element('net')
        doc_edg = etree.ElementTree(net)
        edges = {}
        lanes = {}        
        #       edge
        edges['12_u'] = etree.SubElement(net, 'edge', {'from':'12_input','to':'12_output'}, function = "normal", id = "12_u",\
                                 numLanes = str(5))
        start_coor = (offset_x - x2/2.0 - x3, offset_y - 2.0*lane_width)
        end_coor = (offset_x - x2/2.0, offset_y - 1.5*lane_width)
        lanes['12_u_lane_1'] = etree.SubElement(edges['12_u'], 'lane',index = str(0),\
                                         speed = str(vf), length = str(x1),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0 - x3, offset_y - 1.0*lane_width)
        end_coor = (offset_x - x2/2.0, offset_y - 0.5*lane_width)
        lanes['12_u_lane_2'] = etree.SubElement(edges['12_u'], 'lane',index = str(1),\
                                         speed = str(vf), length = str(x1),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0 - x3, offset_y)
        end_coor = (offset_x - x2/2.0, offset_y + 0.5*lane_width)
        lanes['12_u_lane_3'] = etree.SubElement(edges['12_u'], 'lane',index = str(2),\
                                         speed = str(vf), length = str(x1),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0 - x3, offset_y + 1.0*lane_width)
        end_coor = (offset_x - x2/2.0, offset_y + 1.5*lane_width)
        lanes['12_u_lane_4'] = etree.SubElement(edges['12_u'], 'lane',index = str(3),\
                                         speed = str(vf), length = str(x1),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0 - x3, offset_y + 2.0*lane_width)
        end_coor = (offset_x - x2/2.0, offset_y + 2.5*lane_width)
        lanes['12_u_lane_5'] = etree.SubElement(edges['12_u'], 'lane',index = str(4),\
                                         speed = str(vf), length = str(x1),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))

        
        edges['23_u'] = etree.SubElement(net, 'edge', {'from':'12_output','to':'23_output'}, function = "normal", id = "23_u",\
                                 numLanes=str(6))
        start_coor = (offset_x- x2/2.0, offset_y - 2.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y - 2.5*lane_width)
        lanes['23_u_lane_1'] = etree.SubElement(edges['23_u'], 'lane',index = str(0),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0, offset_y - 1.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y - 1.5*lane_width)
        lanes['23_u_lane_2'] = etree.SubElement(edges['23_u'], 'lane',index = str(1),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0, offset_y - 0.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y - 0.5*lane_width)
        lanes['23_u_lane_3'] = etree.SubElement(edges['23_u'], 'lane',index = str(2),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0, offset_y + 0.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y + 0.5*lane_width)
        lanes['23_u_lane_4'] = etree.SubElement(edges['23_u'], 'lane',index = str(3),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x - x2/2.0, offset_y + 1.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y + 1.5*lane_width)
        lanes['23_u_lane_5'] = etree.SubElement(edges['23_u'], 'lane',index = str(4),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        start_coor = (offset_x- x2/2.0, offset_y + 2.5*lane_width)
        end_coor = (offset_x + x2/2.0, offset_y + 2.5*lane_width)
        lanes['23_u_lane_6'] = etree.SubElement(edges['23_u'], 'lane',index = str(5),\
                                         speed = str(vf), length = str(x2),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        edges['34_u'] = etree.SubElement(net, 'edge',{'from':'23_output','to':'34_output'}, function = "normal", id = "34_u",numLanes=str(5))
        #coor of the lanes
        end_coor = (offset_x + x2/2.0 +x3, offset_y - 2.0*lane_width)
        start_coor = (offset_x + x2/2.0, offset_y - 1.5*lane_width)
        lanes['34_u_lane_1'] = etree.SubElement(edges['34_u'], 'lane',index = str(0),\
                                         speed = str(vf), length = str(x3),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        end_coor = (offset_x + x2/2.0 +x3, offset_y - 1.0*lane_width)
        start_coor = (offset_x + x2/2.0, offset_y - 0.5*lane_width)
        lanes['34_u_lane_2'] = etree.SubElement(edges['34_u'], 'lane',index = str(1),\
                                         speed = str(vf), length = str(x3),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        end_coor = (offset_x + x2/2.0 +x3, 1.0*offset_y)
        start_coor = (offset_x + x2/2.0, offset_y + 0.5*lane_width)
        lanes['34_u_lane_3'] = etree.SubElement(edges['34_u'], 'lane',index = str(2),\
                                         speed = str(vf), length = str(x3),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        end_coor = (offset_x + x2/2.0 +x3, offset_y + 1.0*lane_width)
        start_coor = (offset_x + x2/2.0, offset_y + 1.5*lane_width)
        lanes['34_u_lane_4'] = etree.SubElement(edges['34_u'], 'lane',index = str(3),\
                                         speed = str(vf), length = str(x3),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        end_coor = (offset_x + x2/2.0 +x3, offset_y + 2.0*lane_width)
        start_coor = (offset_x + x2/2.0, offset_y + 2.5*lane_width)
        lanes['34_u_lane_5'] = etree.SubElement(edges['34_u'], 'lane',index = str(4),\
                                         speed = str(vf), length = str(x3),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
                
        edges['52_u'] = etree.SubElement(net, 'edge',{'from':'52_input','to':'12_output'} ,function = "normal", id = "52_u",\
                                  numLanes=str(1))
        
        start_coor = (offset_x - x4/((2**0.5)*1.0) -x2/2.0, offset_y - x4/((2**0.5)*1.0))
        end_coor = (offset_x - x2/2.0  , offset_y - 2.5*lane_width)
        lanes['52_u_lane_1'] = etree.SubElement(edges['52_u'], 'lane',index = str(0),\
                                         speed = str(vf), length = str(x4),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        
        #36 U-section
        edges['36_u'] = etree.SubElement(net, 'edge', {'from':'23_output','to':'36_output'} ,function = "normal", id = "36_u",\
                                  numLanes=str(1))
        start_coor = (offset_x + x2/2.0 , offset_y - 2.5*lane_width)
        end_coor = (offset_x + x5/((2**0.5)*1.0) + x2/2.0, offset_y - x5/(1.0*(2**0.5)))
        lanes['36_u_lane_1'] = etree.SubElement(edges['36_u'], 'lane',index = str(0),\
                                         speed = str(vf), length = str(x5),\
                                    shape = str(start_coor[0])+','+str(start_coor[1])+' '+str(end_coor[0])+','+str(end_coor[1]))
        
        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc_edg))
        outFile.close()



def Generate_node_file(filename = sumo_file_folder + 'ArterialIntersection.nod.xml',x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100,offsetx = 0,offsety = 0, lane_width = 3.5):
        #generate node file
        nodes = etree.Element('nodes')
        doc_node = etree.ElementTree(nodes)
        etree.SubElement(nodes, 'node', id = '12_input', \
                                     x = str(offsetx-x2/2.0-x1),\
                                     y = str(offsety+0))
                                    
        etree.SubElement(nodes, 'node', id = '12_output', x = str(-x2/2.0+offsetx),y = str(0.0+offsety))
        
        etree.SubElement(nodes, 'node', id = '34_output', \
                                     x = str(x2/2.0+x3+offsetx),\
                                     y = str(0.0+offsety))
                                     
        etree.SubElement(nodes, 'node', id = '36_output',\
                                     y = str(-x5/(1.0*(2**0.5))+offsety),\
                                     x = str(x5/(1.0*(2**0.5))+x2/2.0+offsetx))

        etree.SubElement(nodes, 'node', id = '52_input', \
                                     y = str(-x4/(1.0*(2**0.5))+offsety),\
                                     x = str(-x4/(1.0*(2**0.5))-x2/2.0+offsetx))

        etree.SubElement(nodes, 'node', id = '23_output', \
                                     x = str(x2/2.0+offsetx),\
                                     y = str(0.0+offsety))
    
        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc_node))
        outFile.close()
    


def connection_file(filename = sumo_file_folder + 'ArterialIntersection.con.xml'):
        """
        note that, the last several lines define the signals in con.xml
        ----------------------------------------------
        Input: edges, a dict
                edges['east'] is also a dict, keys include 'east_c', 'east_u','east_out'
        Input: lanes, a dict. 
                
        """
        connections = etree.Element('connections')
        doc_connections = etree.ElementTree(connections)
        

        #at the interface
        etree.SubElement(connections, 'connection',{'from':'12_u','to':'23_u'},{'fromLane':'0','toLane':'1'})
        etree.SubElement(connections, 'connection',{'from':'12_u','to':'23_u'},{'fromLane':'1','toLane':'2'})
        etree.SubElement(connections, 'connection',{'from':'12_u','to':'23_u'},{'fromLane':'2','toLane':'3'})
        etree.SubElement(connections, 'connection',{'from':'12_u','to':'23_u'},{'fromLane':'3','toLane':'4'})
        etree.SubElement(connections, 'connection',{'from':'12_u','to':'23_u'},{'fromLane':'4','toLane':'5'})
        
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'34_u'},{'fromLane':'1','toLane':'0'})
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'34_u'},{'fromLane':'2','toLane':'1'})
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'34_u'},{'fromLane':'3','toLane':'2'})
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'34_u'},{'fromLane':'4','toLane':'3'})
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'34_u'},{'fromLane':'5','toLane':'4'})
        
        etree.SubElement(connections, 'connection',{'from':'23_u','to':'36_u'},{'fromLane':'0','toLane':'0'})

        etree.SubElement(connections, 'connection',{'from':'52_u','to':'23_u'},{'fromLane':'0','toLane':'0'})
        

        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc_connections))
        outFile.close()
        

def Generate_rou_dynamic_file(filename = sumo_file_folder + 'ArterialIntersection_dynamic.rou.xml', Q1 = 1400, Q2 = 500, Q3 = 1200, Q4 = 500):
        """
        Input: dai_demands
                dict, keys are ['east', 'south', 'north','west']
                dai_demands['east'] = {'left':RouteDemand, 'through':RouteDemand, 'right':RouteDemand}                
        """
        routes = etree.Element('routes')
        doc_rou = etree.ElementTree(routes)
        etree.SubElement(routes, 'vType',{'id':'type1','accel':'3.0','decel':'4.5','sigma':'0.5'},\
                         {'length':'5','maxSpeed':'120'})
        # demand
        q1 = etree.SubElement(routes, 'flow',{'id':'type_12_1','begin':'0','end':'7200',\
                                         'probability':str(Q1/3600),'type':'type1'})
        etree.SubElement(q1, 'route',{'edges':'12_u 23_u 34_u'})
        
        q2 = etree.SubElement(routes, 'flow',{'id':'type_12_2','begin':'0','end':'7200',\
                                         'probability':str(Q2/3600),'type':'type1'})
        etree.SubElement(q2, 'route',{'edges':'12_u 23_u 36_u'})
        
        q3 = etree.SubElement(routes, 'flow',{'id':'type_52_1','begin':'0','end':'7200',\
                                         'probability':str(Q3/3600),'type':'type1'})
        etree.SubElement(q3, 'route',{'edges':'52_u 23_u 34_u'})
        
        q4 = etree.SubElement(routes, 'flow',{'id':'type_52_2','begin':'0','end':'7200',\
                                         'probability':str(Q4/3600),'type':'type1'})
        etree.SubElement(q4, 'route',{'edges':'52_u 23_u 36_u'})


        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc_rou))
        outFile.close()
    


def Generate_additional_elements(filename = sumo_file_folder + 'ArterialIntersection.add.xml',loop_freq = '30',
                                 probe_freq = '3',
                                 edge_freq = '30',
                                 x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100):
        """
        Revised: signals_elements should be set in **.tll.xml file. 
        --------------------------------------------------------
        Input: signal_element
            etree.Element instance. It shoudl be generated in Generate_signals_elements().
        Input: loop_freq
                the frequency of the loop detector
        Input: probe_freq
                the frequency of the probe vehicle
        input: TLS_ID
            the ID of the signals. 
        """
        additional = etree.Element('additional')
        doc_add = etree.ElementTree(additional)
        

        #detector
        #       12 u
        etree.SubElement(additional, 'inductionLoop',{'id':'12_u_0','lane':'12_u_0','pos':'x1/2','freq':loop_freq,'file':'loop_12_u_0.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'12_u_1','lane':'12_u_1','pos':'x1/2','freq':loop_freq,'file':'loop_12_u_1.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'12_u_2','lane':'12_u_2','pos':'x1/2','freq':loop_freq,'file':'loop_12_u_2.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'12_u_3','lane':'12_u_3','pos':'x1/2','freq':loop_freq,'file':'loop_12_u_3.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'12_u_4','lane':'12_u_4','pos':'x1/2','freq':loop_freq,'file':'loop_12_u_4.xml'})
        #       23_u
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_0','lane':'23_u_0','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_0.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_1','lane':'23_u_1','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_1.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_2','lane':'23_u_2','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_2.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_3','lane':'23_u_3','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_3.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_4','lane':'23_u_4','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_4.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'23_u_5','lane':'23_u_5','pos':'x2/2','freq':loop_freq,'file':'loop_23_u_5.xml'})
        #       34 out
        etree.SubElement(additional, 'inductionLoop',{'id':'34_u_0','lane':'34_u_0','pos':'x3/2','freq':loop_freq,'file':'loop_34_u_0.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'34_u_1','lane':'34_u_1','pos':'x3/2','freq':loop_freq,'file':'loop_34_u_1.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'34_u_2','lane':'34_u_2','pos':'x3/2','freq':loop_freq,'file':'loop_34_u_2.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'34_u_3','lane':'34_u_3','pos':'x3/2','freq':loop_freq,'file':'loop_34_u_3.xml'})
        etree.SubElement(additional, 'inductionLoop',{'id':'34_u_4','lane':'34_u_4','pos':'x3/2','freq':loop_freq,'file':'loop_34_u_4.xml'})
        #       north u
        etree.SubElement(additional, 'inductionLoop',{'id':'52_u_0','lane':'52_u_0','pos':'x4/2','freq':loop_freq,'file':'loop_52_u_0.xml'})
        
        etree.SubElement(additional, 'inductionLoop',{'id':'36_u_0','lane':'36_u_0','pos':'x5/2','freq':loop_freq,'file':'loop_36_u_0.xml'})

        #vehicle probes
        etree.SubElement(additional, 'vTypeProbe',{'id':'probe1','type':'type1','freq':probe_freq,'file':'probe1.xml'})
        
        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc_add))
        outFile.close()



def Generate_sumocfg_file(filename = sumo_file_folder + 'ArterialIntersection.sumocfg', net_file = "ArterialIntersection.net.xml", rou_file = "ArterialIntersection.rou.xml", add_file = "ArterialIntersection.add.xml", end_moment = 3600.0):
        """
        Input: net_file, rou_file, add_file
        
        """
        
        configuration = etree.Element('configuration')
        doc = etree.ElementTree(configuration)
        #begin and end moment
        timee = etree.SubElement(configuration, 'time')
        etree.SubElement(timee, 'begin',value="0")
        etree.SubElement(timee, 'end',value=str(end_moment))
        
        #input files definition
        inputt = etree.SubElement(configuration, 'input')
        
        etree.SubElement(inputt, 'net-file',value=net_file)
        etree.SubElement(inputt, 'route-files',value=rou_file)
        etree.SubElement(inputt, 'additional-files',value=add_file)
        #output files definiton
        output = etree.SubElement(configuration, 'output')
        etree.SubElement(output, 'netstate-dump',value="output.xml")
        
        outFile = open(filename, 'wb')
        outFile.write(etree.tostring(doc))
        outFile.close()
        

def Generate_all_sumo_files(filename_prefix = sumo_file_folder + 'ArterialIntersection.',Q1 = 1400, Q2 = 500, Q3 = 1200, Q4 = 500, x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100,vf = 120, loop_freq = '30', probe_freq = '3', edge_freq = '30', end_moment = 7200.0):
        """
        Generate all files for sumo simulation includeing:
                nod.xml
                rou.xml
                edg.xml
                con.xml
                add.xml
                sumocfg
        Steps:
                nod.xml
                rou.xml
                edg.xml
                con.xml
                add.xml
        """
        #nod.xml
        nodefilename = filename_prefix+'nod.xml'
        Generate_node_file(filename = nodefilename,x1 = x1,x2 = x2,x3 = x3,x4 = x4,x5 = x5)
        
        
        #rou.xml
        roufilename = filename_prefix + 'rou.xml'
        Generate_rou_dynamic_file(filename = roufilename, Q1 = Q1, Q2 = Q2, Q3 = Q3, Q4 = Q4)
        
        
        #edg.xml
        edgfilename = filename_prefix + 'edg.xml'
        Generate_edge_elements_approach(filename = edgfilename,x1 = x1,x2 = x2,x3 = x3,x4 = x4,x5 = x5,vf = vf)
      
        
        #con.xml
        confilename = filename_prefix + 'con.xml'
        connection_file(filename = confilename)
        
        #add.xml
        addfilename = filename_prefix + 'add.xml'
        Generate_additional_elements(filename = addfilename,loop_freq = loop_freq, probe_freq = probe_freq, edge_freq = edge_freq,x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100)        
        
        
Generate_all_sumo_files(filename_prefix = sumo_file_folder + 'ArterialIntersection.',Q1 = 1400, Q2 = 500, Q3 = 1200, Q4 = 500, x1 = 200,x2 = 100,x3 = 200,x4 = 100,x5 = 100,vf = 120, loop_freq = '30', probe_freq = '3', edge_freq = '30', end_moment = 7200.0)    


def netconvert(sumo_file_folder, filename='ArterialIntersection'):
        """
        exec the netconvert
        """
        cmd1 = "cd "+sumo_file_folder
        cmd2 = "netconvert --node-files="+filename+".nod.xml "+\
                                        "--edge-files="+filename+".edg.xml "+\
                                "--connection-files="+filename+".con.xml "+\
                                        "--output-file="+filename+".net.xml"
        os.system(cmd1 + ' && '+ cmd2)
        
netconvert(sumo_file_folder=sumo_file_folder, filename='ArterialIntersection') 
       
#sumocfg
Generate_sumocfg_file(filename = filename_prefix + 'sumocfg', net_file = filename_prefix + '.net.xml', rou_file = filename_prefix + '.rou.xml', add_file = filename_prefix + '.add.xml', end_moment = 7200.0)
