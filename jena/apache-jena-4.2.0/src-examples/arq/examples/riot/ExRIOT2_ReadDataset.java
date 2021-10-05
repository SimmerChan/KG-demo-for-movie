/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package arq.examples.riot;

import static org.apache.jena.riot.RDFLanguages.TRIG ;
import org.apache.jena.query.Dataset ;
import org.apache.jena.query.DatasetFactory ;
import org.apache.jena.riot.RDFDataMgr ;

/** Example of using RIOT : reading data into datasets. */
public class ExRIOT2_ReadDataset
{
    public static void main(String...argv)
    {
        Dataset ds = null ;
        
        // Read a TriG file into quad storage in-memory.
        ds = RDFDataMgr.loadDataset("data.trig") ;
        
        // read some (more) data into a dataset graph.
        RDFDataMgr.read(ds, "data2.trig") ;
        
        // Create a dataset,
        Dataset ds2 = DatasetFactory.createTxnMem() ;
        // read in data, indicating the syntax in case the remote end does not
        // correctly provide the HTTP content type.
        RDFDataMgr.read(ds2, "http://host/data2.unknown", TRIG) ;
    }
}
