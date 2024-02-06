<%@include file="db.jsp" %> <%@page import="java.sql.*" %> <%@ page
language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>join</title>
    <link href="style.css" rel="stylesheet" />
  </head>
  <body>
    <jsp:include page="header.jsp" />
    <script type="text/javascript" src="check.js"></script>
    <section>
      <h2 style="text-align: center"><b>선수 등록</b></h2>
      <form
        method="post"
        action="action.jsp"
        name="frm"
        style="display: flex; align-items: center; justify-content: center"
      >
        <input type="hidden" name="mode" value="insert" />
        <table border="1" style="width: 20%; height: 20%; text-align: center">
          <% request.setCharacterEncoding("UTF-8"); String pid = ""; try {
          String sql = "SELECT MAX(pid)+1 FROM giants_player"; PreparedStatement
          pstmt = conn.prepareStatement(sql); ResultSet rs =
          pstmt.executeQuery(sql); rs.next(); pid = rs.getString(1); } catch
          (Exception e) { e.printStackTrace(); } %>
          <tr>
            <td>선수번호</td>
            <td>
              <input
                type="text"
                name="pid"
                value="<%=pid%>"
                style="width: 96%"
                readonly
              />
            </td>
          </tr>
          <tr>
            <td>선수이름</td>
            <td><input type="text" name="pname" style="width: 96%" /></td>
          </tr>
          <tr>
            <td>선수포지션</td>
            <td>
              <select name="pposition" style="width: 96%">
                <option value="">포지션선택</option>
                <option value="투수">투수</option>
                <option value="내야수">내야수</option>
                <option value="외야수">외야수</option>
                <option value="포수">포수</option>
              </select>
            </td>
          </tr>
          <tr>
            <td>선수등록일</td>
            <td><input type="text" name="pdate" style="width: 96%" /></td>
          </tr>
          <tr>
            <td>선수등급</td>
            <td>
              <input type="radio" name="pgrade" value="S" /> S
              <input type="radio" name="pgrade" value="A" /> A
              <input type="radio" name="pgrade" value="B" /> B
              <input type="radio" name="pgrade" value="C" /> C
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <input type="button" value="등록" onclick="return joinCheck()" />
              <input type="button" value="다시쓰기" onclick="return resett()" />
            </td>
          </tr>
        </table>
      </form>
    </section>
    <jsp:include page="footer.jsp" />
  </body>
</html>
