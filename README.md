# Generate-Collections-for-Mongodb-in-Python

The programe written in Python which will help administrator/learner who wish to generate the testing collections in MongoDB.
The code designed not only for MongoDB, it can be used to generate some of popular Databases like MySQL, SQLPLUS ...

# Advantanges

+ The accuracy of the tool is: 98%
+ It can generate a big data within 1 minutes. The code is designed for 10,000 testing data with random real name of people and random
birthday for itself.
+ It can be used to apply for many Database programming languages.
+ It can filter the variable which the administrator/learner want to work on with statement to give a correct data.
+ It can define the interval for birthday (datetime) which is really useful to give a proper result.
+ Because it was writtern in Python, thus it probably can be able to run on many OS evironment (Windows, Linux, OSX..)

# Disadvantanges

+ Because it was created by a good filter by name's pattern, so the data given out is sometimes will be lesser than given requirements.
For example here: the obligatory result is 10,000 data
                  Because of the filter, it just give 99,996 correct data and 4 data left was removed by filter.
+ After giving out the data to the text files or .sql files, the  administrator/learner need to find the way to input to the command
interface which is not convenient.

# Requirement from Lecturer:
<html>
<p>Insert data to the database that would give for the following results for these 5 queries:</p>
	<table>
		<tr><th>Query</th><th>Result</th><th>Comment</th></tr>
		<tr>
			<td><pre>db.clients.count();</pre></td>
			<td style="text-align: right; padding: 0 10px; font-weight: bold;">10000</td>
			<td>Total number of documents</td>
		</tr>
		<tr>
			<td><pre>db.clients.find({"birthdate":{"$lt":"1990-01-01"}}).count()</pre></td>
			<td style="text-align: right; padding: 0 10px; font-weight: bold;">6000</td>
			<td>"birthdate" is less than (before) "1990-01-01"</td>
		</tr>
		<tr>
			<td><pre>db.clients.find({"birthdate":{"$gt":"1980-01-01"}}).count()</pre></td>
			<td style="text-align: right; padding: 0 10px; font-weight: bold;">6000</td>
			<td>"birthdate" is greater than "1980-01-01"</td>
		</tr>
		<tr>
			<td><pre>db.clients.find({"name":"Tom"}).count()</pre></td>
			<td style="text-align: right; padding: 0 10px; font-weight: bold;">100</td>
			<td>"name" is "Tom"</td>
		</tr>
		<tr>
			<td><pre>db.clients.find({"name":{"$regex":"^Tom"}}).count()</pre></td>
			<td style="text-align: right; padding: 0 10px; font-weight: bold;">200</td>
			<td>"name" starts with "Tom"</td>
		</tr>
	</table>
</html>
#Result:

