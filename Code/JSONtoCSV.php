<?php

function JSONtoCSV()
{
    $groups = array("cited_patents","inventors","application_citations","applications","assignees","citedby_patents"," coinventors","cpc_subgroups", "cpc_subsections","cpcs", "ipcs","locations", "nber_subcategories","nbers","patents","uspc_mainclasses", "uspc_subclasses","uspcs","years");
    $array = json_decode($jsonData, true);
    
}
JSONtoCSV()

?> 